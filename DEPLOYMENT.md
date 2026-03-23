# Deployment Guide

Complete guide for deploying the E-Learning Platform to production.

## Pre-Deployment Checklist

- [ ] Change `DEBUG = False`
- [ ] Generate new `SECRET_KEY`
- [ ] Set up database (MySQL/PostgreSQL)
- [ ] Configure SSL/TLS certificate
- [ ] Set `ALLOWED_HOSTS`
- [ ] Configure email backend
- [ ] Enable `SECURE_SSL_REDIRECT = True`
- [ ] Run `python manage.py check --deploy`
- [ ] Set up log rotation
- [ ] Configure backup strategy
- [ ] Enable monitoring/alerting

---

## 1. Environment Preparation

### Generate Secure Secret Key

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### Create Production .env

```env
DEBUG=False
SECRET_KEY=<generated-key-from-above>
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com

# Database Configuration
DATABASE_ENGINE=django.db.backends.mysql
DATABASE_NAME=elearning_prod
DATABASE_USER=elearning_user
DATABASE_PASSWORD=<strong-password>
DATABASE_HOST=db.yourdomain.com
DATABASE_PORT=3306

# Security
SECURE_SSL_REDIRECT=True
SESSION_COOKIE_SECURE=True
CSRF_COOKIE_SECURE=True
SECURE_HSTS_SECONDS=31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS=True
SECURE_HSTS_PRELOAD=True

# Email
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-specific-password

# CORS
CORS_ALLOWED_ORIGINS=https://yourdomain.com,https://www.yourdomain.com
```

---

## 2. Server Setup

### Install Dependencies

```bash
# Update system packages
sudo apt-get update
sudo apt-get upgrade

# Install required packages
sudo apt-get install -y python3-pip python3-venv python3-dev
sudo apt-get install -y mysql-server mysql-client
sudo apt-get install -y nginx
sudo apt-get install -y supervisor
```

### Create Application User

```bash
sudo useradd -m -s /bin/bash elearning
sudo su - elearning
```

### Clone Application

```bash
cd /home/elearning
git clone <repository-url> app
cd app
```

### Setup Python Environment

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install gunicorn
```

---

## 3. Database Setup (MySQL)

### Create Database and User

```bash
sudo mysql -u root -p
```

```sql
CREATE DATABASE elearning_prod;
CREATE USER 'elearning_user'@'localhost' IDENTIFIED BY 'strong_password_here';
GRANT ALL PRIVILEGES ON elearning_prod.* TO 'elearning_user'@'localhost';
FLUSH PRIVILEGES;
EXIT;
```

### Run Migrations

```bash
python manage.py migrate
```

### Create Superuser

```bash
python manage.py createsuperuser
```

---

## 4. Static & Media Files

### Collect Static Files

```bash
python manage.py collectstatic --noinput
```

### Configure Directories

```bash
mkdir -p /var/www/elearning/{static,media}
sudo chown -R elearning:elearning /var/www/elearning
```

---

## 5. Gunicorn Configuration

### Create Gunicorn Socket

Create `/etc/systemd/system/elearning.socket`:

```ini
[Unit]
Description=gunicorn socket for elearning

[Socket]
ListenStream=127.0.0.1:8000

[Install]
WantedBy=sockets.target
```

### Create Gunicorn Service

Create `/etc/systemd/system/elearning.service`:

```ini
[Unit]
Description=elearning gunicorn daemon
Requires=elearning.socket
After=network.target

[Service]
Type=notify
User=elearning
Group=www-data
WorkingDirectory=/home/elearning/app
EnvironmentFile=/home/elearning/app/.env
ExecStart=/home/elearning/app/venv/bin/gunicorn \
          --workers 4 \
          --worker-class sync \
          --timeout 120 \
          --bind unix:/run/gunicorn.sock \
          config.wsgi:application

[Install]
WantedBy=multi-user.target
```

### Enable and Start Gunicorn

```bash
sudo systemctl daemon-reload
sudo systemctl enable elearning elearning.socket
sudo systemctl start elearning.socket elearning
```

---

## 6. Nginx Configuration

### Create Nginx Config

Create `/etc/nginx/sites-available/elearning`:

```nginx
upstream gunicorn {
    server unix:/run/gunicorn.sock fail_timeout=0;
}

server {
    listen 80;
    server_name yourdomain.com www.yourdomain.com;

    # Redirect HTTP to HTTPS
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl http2;
    server_name yourdomain.com www.yourdomain.com;

    # SSL Certificate
    ssl_certificate /etc/ssl/certs/yourdomain.com.crt;
    ssl_certificate_key /etc/ssl/private/yourdomain.com.key;

    # SSL Configuration
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers HIGH:!aNULL:!MD5;
    ssl_prefer_server_ciphers on;

    # Security Headers
    add_header Strict-Transport-Security "max-age=31536000; includeSubDomains" always;
    add_header X-Content-Type-Options "nosniff" always;
    add_header X-Frame-Options "DENY" always;
    add_header X-XSS-Protection "1; mode=block" always;

    client_max_body_size 50M;

    location /static/ {
        alias /var/www/elearning/static/;
        expires 30d;
        add_header Cache-Control "public, immutable";
    }

    location /media/ {
        alias /var/www/elearning/media/;
        expires 7d;
    }

    location / {
        proxy_pass http://gunicorn;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_redirect off;
        proxy_buffering off;
        proxy_request_buffering off;
    }
}
```

### Enable Nginx Config

```bash
sudo ln -s /etc/nginx/sites-available/elearning /etc/nginx/sites-enabled/
sudo systemctl restart nginx
```

---

## 7. SSL/TLS Certificate (Let's Encrypt)

### Install Certbot

```bash
sudo apt-get install -y certbot python3-certbot-nginx
```

### Generate Certificate

```bash
sudo certbot certonly --nginx -d yourdomain.com -d www.yourdomain.com
```

### Auto-Renewal

```bash
sudo systemctl enable certbot.timer
sudo systemctl start certbot.timer
```

---

## 8. Logging & Monitoring

### Create Log Directory

```bash
sudo mkdir -p /var/log/elearning
sudo chown elearning:www-data /var/log/elearning
```

### Configure Log Rotation

Create `/etc/logrotate.d/elearning`:

```
/var/log/elearning/*.log {
    daily
    rotate 30
    compress
    delaycompress
    notifempty
    create 0640 elearning www-data
    sharedscripts
    postrotate
        systemctl restart elearning
    endscript
}
```

### Monitor Application

```bash
# Check service status
sudo systemctl status elearning

# View logs
sudo journalctl -u elearning -f

# View Nginx logs
sudo tail -f /var/log/nginx/access.log
sudo tail -f /var/log/nginx/error.log
```

---

## 9. Database Backups

### Automated Backup Script

Create `/home/elearning/backup.sh`:

```bash
#!/bin/bash
BACKUP_DIR="/backups/elearning"
DATE=$(date +%Y%m%d_%H%M%S)

mkdir -p $BACKUP_DIR

mysqldump -u elearning_user -p$DB_PASSWORD elearning_prod | \
  gzip > $BACKUP_DIR/elearning_$DATE.sql.gz

# Keep only last 30 days
find $BACKUP_DIR -type f -mtime +30 -delete

echo "Backup completed: $BACKUP_DIR/elearning_$DATE.sql.gz"
```

### Schedule Backup with Cron

```bash
# Edit crontab
crontab -e

# Add line for daily backup at 2 AM
0 2 * * * /home/elearning/backup.sh
```

---

## 10. Security Hardening

### Firewall Configuration

```bash
sudo ufw enable
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow 22/tcp      # SSH
sudo ufw allow 80/tcp      # HTTP
sudo ufw allow 443/tcp     # HTTPS
sudo ufw status
```

### Fail2Ban Setup

```bash
sudo apt-get install -y fail2ban

# Create local configuration
sudo cp /etc/fail2ban/jail.conf /etc/fail2ban/jail.local

# Edit and enable
sudo systemctl enable fail2ban
sudo systemctl start fail2ban
```

### SSH Hardening

Edit `/etc/ssh/sshd_config`:

```
PermitRootLogin no
PasswordAuthentication no
PubkeyAuthentication yes
Protocol 2
Port 2222  # Change default port
```

---

## 11. Monitoring & Alerting

### Setup Sentry (Error Tracking)

1. Create account at https://sentry.io
2. Create project for Django
3. Get DSN key
4. Add to `.env`:
   ```
   SENTRY_DSN=https://key@sentry.io/project-id
   ```

### Monitor with New Relic (Optional)

```bash
pip install newrelic
newrelic-admin generate-config YOUR_LICENSE_KEY newrelic.ini
```

---

## 12. Performance Optimization

### Enable Caching

```python
# settings.py
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
    }
}
```

### Database Connection Pooling

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'CONN_MAX_AGE': 600,  # 10 minutes
    }
}
```

### CDN Configuration

Serve static files via CloudFront, CloudFlare, or similar.

---

## 13. Testing Deployment

### Security Check

```bash
python manage.py check --deploy
```

### Test Email

```bash
python manage.py shell
from django.core.mail import send_mail
send_mail('Test', 'This is a test', 'noreply@yourdomain.com', ['your@email.com'])
```

### Test API

```bash
curl https://yourdomain.com/api/
```

---

## 14. Troubleshooting Deployment

### Application Won't Start

```bash
# Check logs
sudo journalctl -u elearning -n 50

# Check syntax
python manage.py check
```

### Database Connection Issues

```bash
# Test from server
mysql -u elearning_user -p -h localhost elearning_prod

# Check Django connection
python manage.py dbshell
```

### Static Files Not Serving

```bash
# Recollect and check permissions
python manage.py collectstatic --clear --noinput
ls -la /var/www/elearning/static/
```

### High Memory Usage

```bash
# Adjust Gunicorn workers
--workers 2  # Instead of 4

# Check running processes
ps aux | grep gunicorn
```

---

## Maintenance Commands

### Update Dependencies

```bash
source venv/bin/activate
pip install --upgrade -r requirements.txt
```

### Run Database Migrations

```bash
python manage.py migrate
```

### Create Cache Table

```bash
python manage.py createcachetable
```

### Clear Expired Sessions

```bash
python manage.py clearsessions
```

---

## Rollback Procedure

### If deployment fails:

```bash
# Stop application
sudo systemctl stop elearning

# Restore previous version
cd /home/elearning/app
git checkout previous_version

# Restart
sudo systemctl start elearning
```

---

## Further Reading

- Django Deployment Checklist: https://docs.djangoproject.com/en/stable/howto/deployment/checklist/
- Gunicorn Docs: https://docs.gunicorn.org/
- Nginx Docs: https://nginx.org/en/docs/
- Let's Encrypt: https://letsencrypt.org/

---

**Deployment completed successfully! 🚀**
