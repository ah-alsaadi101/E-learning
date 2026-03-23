# Quick Start Guide

Get the E-Learning Platform running in 5 minutes!

## Prerequisites

- Python 3.8+ installed
- pip package manager
- 500MB free disk space

## Quick Setup (Windows)

### 1. Clone/Download Project

```bash
cd your-projects-folder
# Extract or clone the project
```

### 2. Run Setup Script

```bash
# Double-click setup.bat
# OR in PowerShell:
.\setup.bat
```

This will:

- Create virtual environment
- Install dependencies
- Setup database
- Create admin account

### 3. Start Server

```bash
python manage.py runserver
```

### 4. Access Application

- **Web**: http://localhost:8000
- **Admin**: http://localhost:8000/admin
- **API**: http://localhost:8000/api/

---

## Quick Setup (macOS/Linux)

### 1. Clone/Download Project

```bash
cd your-projects-folder
# Extract or clone the project
```

### 2. Run Setup Script

```bash
chmod +x setup.sh
./setup.sh
```

### 3. Start Server

```bash
python manage.py runserver
```

### 4. Access Application

- **Web**: http://localhost:8000
- **Admin**: http://localhost:8000/admin
- **API**: http://localhost:8000/api/

---

## Manual Setup (If Setup Script Fails)

### Step 1: Create Virtual Environment

```bash
python -m venv venv

# Activate it
# Windows:
venv\Scripts\activate.bat
# macOS/Linux:
source venv/bin/activate
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Setup Database

```bash
python manage.py migrate
```

### Step 4: Create Admin Account

```bash
python manage.py createsuperuser
```

Follow prompts to set username, email, password.

### Step 5: Run Server

```bash
python manage.py runserver
```

---

## Login & Test

1. Go to http://localhost:8000/admin
2. Login with your superuser credentials
3. You'll see the admin dashboard

---

## First Steps

### 1. Create Some Data in Admin

- Add a **Category** (e.g., "Programming")
- Create a **Course** (e.g., "Python Basics")
- Add some **Lessons** to the course
- Create a **Quiz** with questions

### 2. Test Web Interface

- Go to http://localhost:8000
- Click "Courses"
- You'll see your created courses

### 3. Test API

- Go to http://localhost:8000/api/
- Browse the REST API interface
- Get an authentication token from `/api/accounts/users/login/`

---

## Common Issues & Solutions

### "ModuleNotFoundError: No module named 'django'"

**Solution:** Ensure virtual environment is activated

```bash
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

### "Port 8000 is already in use"

**Solution:** Use a different port

```bash
python manage.py runserver 8080
# Then access http://localhost:8080
```

### "Database is locked"

**Solution:** Delete db.sqlite3 and migration files (development only)

```bash
rm db.sqlite3
python manage.py migrate
```

### "Static files not loading"

**Solution:** Collect static files

```bash
python manage.py collectstatic --noinput
```

---

## Environment Variables (.env)

Create a `.env` file in the project root:

```env
DEBUG=True
SECRET_KEY=your-secret-key
ALLOWED_HOSTS=localhost,127.0.0.1
```

See `.env.example` for all available options.

---

## File Locations

- **Database**: `db.sqlite3` (development)
- **Media uploads**: `media/`
- **Static files**: `static/`
- **Logs**: `logs/`
- **Admin panel**: `/admin/`

---

## User Roles

When creating users, assign these roles:

- **Student**: Can enroll in courses, take quizzes
- **Instructor**: Can create and manage courses
- **Admin**: Full system access

---

## Next Steps

1. Read the full [README.md](README.md) for detailed documentation
2. Check [API_DOCUMENTATION.md](API_DOCUMENTATION.md) for API endpoints
3. Review `DEPLOYMENT.md` for production deployment

---

## Need Help?

- Check error messages carefully
- Run `python manage.py check` to diagnose issues
- See `logs/elearning.log` for detailed error logs
- Review Django documentation: https://docs.djangoproject.com/

---

**Happy Learning! 🚀**
