# E-Learning Platform - Complete Django Project

A production-ready E-Learning platform built with Django and Django REST Framework. This project merges two complete LMS systems into a single, scalable application with both web and API interfaces.

## 📋 Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [Deployment](#deployment)
- [Usage Guide](#usage-guide)
- [API Documentation](#api-documentation)
- [Performance Optimizations](#performance-optimizations)
- [Security Measures](#security-measures)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)

---

## ✨ Features

### Core Features

- ✅ **User Management**: Role-based access (Student, Instructor, Admin)
- ✅ **Course Management**: Create, edit, publish courses with lessons
- ✅ **Enrollment System**: Track student enrollments with payment validation
- ✅ **Quiz System**: Multiple-choice and essay questions with automatic grading
- ✅ **Discussion Forums**: Course-based forums for student interaction
- ✅ **Payment Processing**: Payment tracking and enrollment verification
- ✅ **News & Events**: Announcements and event management
- ✅ **User Dashboards**: Role-specific dashboards for different user types

### Technical Features

- ✅ **REST API**: Full REST API with token authentication
- ✅ **Session Authentication**: Traditional web session auth
- ✅ **Permission System**: Object-level and role-based permissions
- ✅ **Query Optimization**: `select_related` and `prefetch_related` throughout
- ✅ **Caching**: Response caching for improved performance
- ✅ **Logging**: Comprehensive logging with rotating file handlers
- ✅ **Security**: CSRF protection, XSS prevention, secure headers
- ✅ **API Filtering**: Advanced filtering, pagination, and search

---

## 🛠️ Tech Stack

- **Framework**: Django 5.2
- **API**: Django REST Framework 3.15
- **Database**: SQLite (default), PostgreSQL (production-ready)
- **Authentication**: Token Auth + Session Auth
- **Filtering**: django-filter
- **Image Processing**: Pillow
- **Utilities**: model-utils
- **Static Files**: WhiteNoise (production)
- **Deployment**: Railway (free tier supported)
- **Optional**: JWT (djangorestframework-simplejwt), CORS (django-cors-headers)

---

## 📁 Project Structure

```
merged_elearning/
├── config/                          # Project configuration
│   ├── settings.py                 # Django settings (security + performance)
│   ├── urls.py                     # Main URL routing
│   ├── wsgi.py                     # WSGI application
│   └── asgi.py                     # ASGI application
│
├── accounts/                        # User management app
│   ├── models.py                   # Custom User model with roles
│   ├── serializers.py              # DRF serializers
│   ├── api.py                      # REST API viewsets
│   ├── views.py                    # Web views
│   ├── forms.py                    # Django forms
│   ├── admin.py                    # Django admin config
│   └── urls.py/api_urls.py         # URL routing
│
├── courses/                         # Course management app
│   ├── models.py                   # Course, Lesson, Enrollment, Category
│   ├── serializers.py              # Course serializers
│   ├── api.py                      # Course API
│   ├── views.py                    # Course web views
│   ├── admin.py                    # Admin configuration
│   └── urls.py/api_urls.py         # URL routing
│
├── quizzes/                         # Quiz and assessment system
│   ├── models.py                   # Quiz, Question, QuizAttempt
│   ├── serializers.py              # Quiz serializers
│   ├── api.py                      # Quiz API with attempt handling
│   ├── views.py                    # Quiz web interface
│   ├── admin.py                    # Admin configuration
│   └── urls.py/api_urls.py         # URL routing
│
├── payments/                        # Payment management
│   ├── models.py                   # Payment model
│   ├── serializers.py              # Payment serializers
│   ├── api.py                      # Payment API
│   ├── views.py                    # Payment views
│   ├── admin.py                    # Admin configuration
│   └── urls.py/api_urls.py         # URL routing
│
├── discussions/                     # Discussion forums
│   ├── models.py                   # Post, Comment models
│   ├── serializers.py              # Discussion serializers
│   ├── api.py                      # Discussion API
│   ├── views.py                    # Forum views
│   ├── admin.py                    # Admin configuration
│   └── urls.py/api_urls.py         # URL routing
│
├── core/                            # News and events
│   ├── models.py                   # NewsAndEvents model
│   ├── serializers.py              # Core serializers
│   ├── api.py                      # News API
│   ├── views.py                    # News views
│   ├── admin.py                    # Admin configuration
│   └── urls.py/api_urls.py         # URL routing
│
├── templates/                       # HTML templates
│   ├── accounts/                   # Login, register, profile
│   ├── courses/                    # Course list, detail, dashboard
│   ├── quizzes/                    # Quiz interface
│   ├── payments/                   # Payment history
│   ├── discussions/                # Forum pages
│   └── core/                       # News and events pages
│
├── static/                          # Static files (CSS, JS, images)
├── media/                           # User uploads (profiles, course files)
├── logs/                            # Application logs
│
├── manage.py                        # Django management script
├── requirements.txt                 # Python dependencies
├── .env.example                     # Environment variables example
├── README.md                        # This file
└── db.sqlite3                       # SQLite database (development)
```

---

## 🚀 Installation

### Prerequisites

- Python 3.8+ (tested on Python 3.13)
- pip or poetry
- Virtual environment (recommended)
- Git

### Step 1: Clone the Repository

```bash
git clone <repository-url>
cd merged_elearning
```

### Step 2: Create Virtual Environment

**On Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment Variables

```bash
# Copy example environment file
cp .env.example .env

# Edit .env with your settings (see Configuration section)
```

### Step 5: Run Migrations

```bash
python manage.py migrate
```

### Step 6: Create Superuser (Admin Account)

```bash
python manage.py createsuperuser
```

Follow the prompts to create an admin account.

### Step 7: Collect Static Files (Production)

```bash
python manage.py collectstatic --noinput
```

---

## ⚙️ Configuration

### Create `.env` File

Copy `.env.example` to `.env` and update with your settings:

```env
# Debug Mode (False in production)
DEBUG=True
SECRET_KEY=your-secret-key-change-this-in-production

# Allowed Hosts (add your Railway URL for production)
ALLOWED_HOSTS=localhost,127.0.0.1,your-app-name.up.railway.app

# Database (Railway provides DATABASE_URL automatically)
# For local development, defaults to SQLite
# For production, Railway sets DATABASE_URL

# Email Settings (for production)
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend

# Security Settings
SECURE_SSL_REDIRECT=False
SESSION_COOKIE_SECURE=False
CSRF_COOKIE_SECURE=False
```

### Change Secret Key

Generate a new secret key for production:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

---

## 🎯 Running the Application

### Development Server

```bash
python manage.py runserver
```

Access at: `http://localhost:8000`

### Production with Gunicorn

```bash
# Install gunicorn
pip install gunicorn

# Run with gunicorn
gunicorn config.wsgi:application --bind 0.0.0.0:8000 --workers 4
```

### Using Nginx (Advanced)

See deployment guide in `DEPLOYMENT.md`

---

## 🚀 Deployment

### Railway (Free Tier)

This project is configured for easy deployment to Railway.

#### Prerequisites

- GitHub account
- Railway account ([railway.app](https://railway.app))

#### Step 1: Push to GitHub

```bash
git add .
git commit -m "Ready for Railway deployment"
git push origin main
```

#### Step 2: Deploy on Railway

1. Go to [railway.app](https://railway.app) and sign in
2. Click "New Project" → "Deploy from GitHub repo"
3. Connect your GitHub account and select the repository
4. Click "Deploy"

#### Step 3: Add PostgreSQL Database

1. In Railway dashboard, click "Add Plugin"
2. Select "PostgreSQL" (free tier)
3. Railway automatically sets `DATABASE_URL`

#### Step 4: Configure Environment Variables

In Railway service → "Variables", add:

```
SECRET_KEY=your-generated-secret-key
DEBUG=False
ALLOWED_HOSTS=your-app-name.up.railway.app
```

#### Step 5: Run Migrations

In Railway shell:

```bash
python manage.py migrate
python manage.py collectstatic --noinput
```

#### Step 6: Seed Database (Optional)

```bash
python scripts/seed_database.py --clear
```

#### Access Your App

- **Web**: `https://your-app-name.up.railway.app`
- **Admin**: `https://your-app-name.up.railway.app/admin`
- **API**: `https://your-app-name.up.railway.app/api/`

### Other Deployment Options

- **Heroku**: Use `heroku.yml` or buildpacks
- **Render**: Similar to Railway, supports Django
- **AWS/GCP/Azure**: Use Docker or traditional deployment
- **VPS**: See `DEPLOYMENT.md` for full server setup

---

## 📖 Usage Guide

### Admin Interface

1. Start the development server
2. Navigate to: `http://localhost:8000/admin`
3. Log in with superuser credentials
4. Manage users, courses, quizzes, payments, etc.

### Web Interface

#### For Students:

1. Navigate to: `http://localhost:8000`
2. Register as a Student
3. Browse and enroll in courses
4. Take quizzes
5. Participate in discussions
6. View payment history

#### For Instructors:

1. Register as an Instructor
2. Create and manage courses
3. Add lessons and quizzes
4. View enrollment statistics
5. Grade assignments

#### For Admins:

1. Manage all users
2. Moderate discussions
3. View system statistics
4. Manage news and events

### API Endpoints

#### Authentication

```
POST /api/accounts/users/login/ - Login user
POST /api/accounts/users/register/ - Register new user
POST /api/accounts/users/logout/ - Logout user
GET /api/accounts/users/profile/ - Get user profile
```

#### Courses

```
GET /api/courses/categories/ - List categories
GET /api/courses/courses/ - List courses (filterable)
POST /api/courses/courses/ - Create course (instructor only)
GET /api/courses/courses/{id}/ - Get course detail
GET /api/courses/lessons/ - List lessons (filterable)
GET /api/courses/enrollments/ - Get user enrollments
POST /api/courses/enrollments/ - Enroll in course
```

#### Quizzes

```
GET /api/quizzes/quizzes/ - List quizzes
POST /api/quizzes/quizzes/{id}/start_attempt/ - Start quiz attempt
GET /api/quizzes/attempts/ - Get user attempts
POST /api/quizzes/attempts/{id}/submit_answer/ - Submit answer
POST /api/quizzes/attempts/{id}/complete_attempt/ - Complete attempt
```

#### Discussions

```
GET /api/discussions/posts/ - List posts (filterable by course)
POST /api/discussions/posts/ - Create post
POST /api/discussions/posts/{id}/add_comment/ - Add comment
GET /api/discussions/comments/ - List comments
```

#### Payments

```
GET /api/payments/payments/ - Get user payments
POST /api/payments/payments/ - Create payment
```

---

## ⚡ Performance Optimizations

### Database Query Optimization

All views use optimized queries:

- `select_related()` for ForeignKey relationships
- `prefetch_related()` for ManyToMany and reverse FK
- Pagination (20 items per page) to limit large datasets

Example:

```python
# Good - Optimized
courses = Course.objects.select_related('instructor', 'category').prefetch_related('lessons')

# Bad - N+1 queries
courses = Course.objects.all()  # Multiple queries in templates
```

### Caching Strategy

Production settings include caching:

- Page caching for course listings
- Query result caching for frequently accessed data
- Template fragment caching for expensive rendering

```python
# Cache for 1 hour
from django.views.decorators.cache import cache_page
@cache_page(3600)
def course_list(request):
    ...
```

### Response Pagination

All list endpoints paginate results (20 per page):

```
GET /api/courses/courses/?page=1
```

### Database Indexing

Models include field indexing:

- `slug` fields indexed for URL lookups
- `status` fields indexed for filtering
- Foreign keys automatically indexed

### Connection Pooling

For production with large databases:

```python
# In settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'CONN_MAX_AGE': 600,  # Connection pooling
    }
}
```

---

## 🔒 Security Measures

### Built-in Security

1. **CSRF Protection** - Enabled by default
   - All POST/PUT/DELETE requests require CSRF token
   - Tokens automatically validated

2. **SQL Injection Prevention**
   - ORM prevents SQL injection by default
   - Parameterized queries for all database operations

3. **XSS Protection**
   - Automatic HTML escaping in templates
   - Content Security Policy headers
   - No raw HTML in templates by default

4. **Authentication & Authorization**
   - Password hashing with PBKDF2
   - Token-based API authentication
   - Role-based access control (RBAC)
   - Object-level permissions for sensitive data

### Security Headers

All responses include:

- `X-Content-Type-Options: nosniff` - Prevent MIME sniffing
- `X-Frame-Options: DENY` - Prevent clickjacking
- `X-XSS-Protection: 1; mode=block` - Enable browser XSS filter
- `Strict-Transport-Security` (production only)

### Password Requirements

- Minimum 8 characters
- No common passwords (from list of 20,000 common passwords)
- Cannot be similar to username/email
- Hashed with PBKDF2 algorithm

### File Upload Security

- Only allowed file types accepted
- File size limits enforced
- Files stored outside web root
- User-uploaded files served with `X-Sendfile`

### Production Checklist

Before deploying to production:

```bash
# 1. Run security checks
python manage.py check --deploy

# 2. Generate new SECRET_KEY
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

# 3. Update .env settings
DEBUG=False
SECURE_SSL_REDIRECT=True
SESSION_COOKIE_SECURE=True
CSRF_COOKIE_SECURE=True

# 4. Use environment variables for sensitive data
# 5. Enable HTTPS (SSL/TLS)
# 6. Use strong database passwords
# 7. Set up automated backups
# 8. Enable logging for audit trail
```

### API Security

- Token authentication required for sensitive endpoints
- Rate limiting (optional, requires django-ratelimit)
- CORS configuration in `.env`
- Request validation with serializers
- Database-level constraints

---

## 🐛 Troubleshooting

### 1. Migration Errors

```bash
# Reset migrations (development only!)
python manage.py migrate zero <app_label>
python manage.py migrate

# Or start fresh
rm db.sqlite3
python manage.py migrate
```

### 2. Static Files Not Loading

```bash
# Collect static files
python manage.py collectstatic --clear --noinput

# For development, ensure StaticFilesHandler is running
python manage.py runserver 0.0.0.0:8000
```

### 3. Database Connection Issues

```bash
# Check database configuration in .env
# Verify database server is running
# Test connection with Django shell
python manage.py shell
```

### 4. Permission Denied Errors

```bash
# Check user role
# Verify object-level permissions
# Check CSRF token in forms

# In browser console:
document.cookie  # Should show CSRF token
```

### 5. Memory/Performance Issues

```bash
# Enable query logging to find slow queries
python manage.py shell
from django.db import connection
from django.test.utils import CaptureQueriesContext

with CaptureQueriesContext(connection) as context:
    # Your code here
    pass
print(context.captured_queries)

# View execution time
python manage.py runserver --debug-propagate-exceptions
```

---

## 📚 API Examples

### Example 1: User Registration & Login

```bash
# Register
curl -X POST http://localhost:8000/api/accounts/users/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "john",
    "email": "john@example.com",
    "password": "securepass123",
    "role": "student"
  }'

# Login
curl -X POST http://localhost:8000/api/accounts/users/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "john",
    "password": "securepass123"
  }'

# Returns: {"token": "abc123...", "user": {...}}
```

### Example 2: List Courses

```bash
curl -X GET http://localhost:8000/api/courses/courses/ \
  -H "Authorization: Token abc123..." \
  -H "Content-Type: application/json"
```

### Example 3: Enroll in Course

```bash
curl -X POST http://localhost:8000/api/courses/enrollments/ \
  -H "Authorization: Token abc123..." \
  -H "Content-Type: application/json" \
  -d '{
    "course": 1
  }'
```

### Example 4: Submit Quiz Answer

```bash
curl -X POST http://localhost:8000/api/quizzes/attempts/1/submit_answer/ \
  -H "Authorization: Token abc123..." \
  -H "Content-Type: application/json" \
  -d '{
    "question_id": "123",
    "answer": "option_a"
  }'
```

---

## 🧪 Testing

### Run Tests

```bash
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test accounts

# Run with verbose output
python manage.py test --verbosity=2

# Run with coverage
pip install coverage
coverage run --source='.' manage.py test
coverage report
```

---

## 📞 Support & Documentation

- **Django Documentation**: https://docs.djangoproject.com/
- **DRF Documentation**: https://www.django-rest-framework.org/
- **Issue Tracker**: GitHub Issues
- **Email Support**: support@elearning.local

---

## 📝 License

This project is licensed under the MIT License - see LICENSE file for details.

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## ✅ Checklist for Deployment

- [ ] Change DEBUG to False
- [ ] Generate new SECRET_KEY
- [ ] Configure database (PostgreSQL on Railway)
- [ ] Set ALLOWED_HOSTS to Railway URL
- [ ] Configure email backend (optional)
- [ ] Enable SECURE_SSL_REDIRECT (Railway handles SSL)
- [ ] Run `python manage.py check --deploy`
- [ ] Set up log rotation (Railway handles)
- [ ] Configure backup strategy (Railway provides)
- [ ] Enable monitoring/alerting (Railway dashboard)
- [ ] Test API endpoints after deployment

---

**Last Updated**: March 2026  
**Version**: 1.1.0  
**Django Version**: 5.2
