# Quick Reference Card

**E-Learning Platform** | March 23, 2026

---

## 🚀 Start Here

### First Time Setup

```bash
# Option 1: Automated (RECOMMENDED)
cd e:\django\merged_elearning
setup.bat  # Windows
# OR
bash setup.sh  # Linux/Mac

# Option 2: Manual
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### Access Points

| URL                                              | Purpose       | Default         |
| ------------------------------------------------ | ------------- | --------------- |
| `http://localhost:8000`                          | Web Interface | Public          |
| `http://localhost:8000/admin`                    | Admin Panel   | Username: admin |
| `http://localhost:8000/api`                      | API Root      | Token auth      |
| `http://localhost:8000/admin/accounts/user/add/` | Add User      | Admin only      |

---

## 🏗️ Project Structure

```
merged_elearning/
├── config/              → Django settings & URLs
├── accounts/            → User management (60 files)
├── courses/             → Course management
├── quizzes/             → Quiz & assessment
├── payments/            → Payment processing
├── discussions/         → Discussion forums
├── core/                → News & events
├── templates/           → HTML templates
├── static/              → CSS, JS, images
├── logs/                → Application logs
├── db.sqlite3           → Database
├── manage.py            → Django CLI
└── requirements.txt     → Dependencies
```

---

## 📚 Documentation Quick Links

| File                          | Purpose             | Read Time |
| ----------------------------- | ------------------- | --------- |
| `README.md`                   | Overview & features | 10 min    |
| `QUICKSTART.md`               | Setup guide         | 5 min     |
| `API_DOCUMENTATION.md`        | API reference       | 15 min    |
| `DEPLOYMENT.md`               | Production setup    | 20 min    |
| `SECURITY_AND_PERFORMANCE.md` | Security & perf     | 15 min    |
| `PROJECT_COMPLETE_REPORT.md`  | Full inventory      | 30 min    |
| `FILE_INDEX.md`               | File reference      | As needed |
| `PROJECT_OVERVIEW.md`         | Visual summary      | 10 min    |

---

## 🔌 API Quick Reference

### Authentication

```bash
# Register
POST /api/accounts/users/register/
{
  "username": "john",
  "email": "john@example.com",
  "password": "SecurePass123"
}

# Login (get token)
POST /api/accounts/users/login/
{
  "username": "john",
  "password": "SecurePass123"
}

# Use token in headers
Authorization: Token <your_token_here>
```

### Courses

```bash
# List courses
GET /api/courses/?page=1

# Get course details
GET /api/courses/<id>/

# Enroll in course
POST /api/courses/<id>/enroll/

# My courses
GET /api/courses/my_courses/
```

### Quizzes

```bash
# List quizzes
GET /api/quizzes/

# Start quiz
POST /api/quizzes/<id>/start_attempt/

# Submit answer
POST /api/quizzes/attempts/<id>/submit_answer/
{"answer": "A"}

# Complete quiz
POST /api/quizzes/attempts/<id>/complete/
```

### Discussions

```bash
# List discussions
GET /api/discussions/posts/?course_id=1

# Create post
POST /api/discussions/posts/
{
  "title": "Question about ...",
  "content": "...",
  "course": 1
}

# Add comment
POST /api/discussions/<post_id>/add_comment/
{"content": "..."}
```

---

## 🗄️ Model Relationships

```
User
├── courses (instructor)
├── enrollments (student)
├── quiz_attempts
├── posts (author)
├── comments (author)
└── payments

Course
├── lessons
├── enrollments
├── quizzes
├── discussions
└── payments

Quiz
├── questions
└── attempts

Enrollment
├── assignment_score
├── mid_exam_score
├── quiz_score
└── final_exam_score → Auto GPA
```

---

## 🔐 User Roles

| Role           | Can                                       | Cannot                                       |
| -------------- | ----------------------------------------- | -------------------------------------------- |
| **Student**    | Enroll, take quizzes, discuss, pay        | Create courses, grade essays, manage users   |
| **Instructor** | Create courses, add lessons, grade essays | Delete courses (only draft), manage payments |
| **Admin**      | Everything                                | Nothing - has full access                    |

---

## 📝 Common Commands

### Management Commands

```bash
# Create database tables
python manage.py migrate

# Create migrations from models
python manage.py makemigrations

# Create superuser (admin)
python manage.py createsuperuser

# Run development server
python manage.py runserver

# Collect static files (production)
python manage.py collectstatic

# Run tests
python manage.py test

# Access shell
python manage.py shell
```

### Useful Django Shell Operations

```bash
python manage.py shell

# Create user
from accounts.models import User
User.objects.create_user(username='john', email='john@example.com', password='123')

# Create course
from courses.models import Course, Category
cat = Category.objects.create(name='Python')
course = Course.objects.create(title='Python 101', category=cat, instructor=user)

# Enroll student
from courses.models import Enrollment
Enrollment.objects.create(student=user, course=course)

# Exit
exit()
```

---

## 🐛 Troubleshooting

### Migration Issues

```bash
# Reset migrations (development only)
python manage.py migrate accounts zero
python manage.py migrate

# Check migration status
python manage.py showmigrations
```

### Database Issues

```bash
# Delete and recreate database (development only)
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser
```

### Permission Denied

```bash
# Run with admin user
# Create superuser if missing:
python manage.py createsuperuser
```

### Port Already in Use

```bash
# Use different port
python manage.py runserver 8001
```

---

## 🔍 Where to Find Things

| What          | Where                    |
| ------------- | ------------------------ |
| User model    | `accounts/models.py`     |
| Course model  | `courses/models.py`      |
| Quiz model    | `quizzes/models.py`      |
| API endpoints | `*/api.py` in each app   |
| Web URLs      | `*/urls.py` in each app  |
| Forms         | `*/forms.py` in each app |
| Templates     | `templates/<app_name>/`  |
| CSS           | `static/css/`            |
| JavaScript    | `static/js/`             |
| Tests         | `*/tests.py` in each app |
| Admin config  | `*/admin.py` in each app |

---

## 📊 Database Query Examples

```python
# Get all courses
courses = Course.objects.all()

# Get published courses
courses = Course.objects.filter(status='published')

# Get with related data (optimized)
courses = Course.objects.select_related('instructor', 'category')

# Get student's enrollments with grades
enrollments = Enrollment.objects.filter(student=user).select_related('course')

# Get latest quizzes
quizzes = Quiz.objects.order_by('-created_at')[:10]

# Get quiz with questions
quiz = Quiz.objects.prefetch_related('questions').get(id=1)

# Count students in course
student_count = Enrollment.objects.filter(course=course).count()

# Get student's average score
avg_score = Enrollment.objects.filter(student=user).aggregate(
    avg_score=models.Avg('total_score')
)
```

---

## 🔑 Environment Variables (.env)

```env
# Security
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=localhost,127.0.0.1

# Database
DATABASE_ENGINE=django.db.backends.postgresql
DATABASE_NAME=elearning_db
DATABASE_USER=postgres
DATABASE_PASSWORD=password
DATABASE_HOST=localhost
DATABASE_PORT=5432

# Email (optional)
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-password

# Caching (optional)
CACHE_BACKEND=django.core.cache.backends.redis.RedisCache
CACHE_LOCATION=redis://127.0.0.1:6379/1

# Stripe (optional)
STRIPE_SECRET_KEY=sk_test_...
STRIPE_PUBLIC_KEY=pk_test_...
```

---

## ✨ Features at a Glance

### Authentication

- [x] User registration/login
- [x] Token-based API auth
- [x] Session-based web auth
- [x] Password hashing (PBKDF2)
- [x] Role-based access (Student/Instructor/Admin)

### Courses

- [x] Create/edit courses
- [x] Add lessons
- [x] Student enrollment
- [x] Automatic grading
- [x] GPA calculation

### Quizzes

- [x] Multiple choice questions
- [x] Essay questions
- [x] Auto-grading
- [x] Time limits
- [x] Attempt tracking

### Forums

- [x] Discussion posts
- [x] Comments/replies
- [x] Pin/lock posts
- [x] Mark solutions

### Payments

- [x] Process payments
- [x] Multiple methods
- [x] Status tracking
- [x] Auto-enrollment

---

## 🚀 Deployment Checklist

- [ ] Set `DEBUG = False`
- [ ] Generate new `SECRET_KEY`
- [ ] Update `ALLOWED_HOSTS`
- [ ] Configure PostgreSQL/MySQL
- [ ] Set environment variables (.env)
- [ ] Run `python manage.py migrate`
- [ ] Run `python manage.py collectstatic`
- [ ] Set up Gunicorn
- [ ] Configure Nginx
- [ ] Enable HTTPS (SSL)
- [ ] Set up backups
- [ ] Enable logging
- [ ] Configure email service
- [ ] Load test the application

---

## 📞 Support Resources

| Issue                | Solution                                           |
| -------------------- | -------------------------------------------------- |
| Can't login          | Check if user exists: Admin → Users                |
| No courses shown     | Create course as instructor, publish it            |
| Quiz not grading     | Check questions are marked correct                 |
| API auth fails       | Check token header: `Authorization: Token <token>` |
| Static files missing | Run `python manage.py collectstatic`               |
| Database error       | Run `python manage.py migrate`                     |

---

## 📚 Learn More

- **Django 5.2 Docs**: https://docs.djangoproject.com/en/5.2/
- **DRF Serializers**: https://www.django-rest-framework.org/api-guide/serializers/
- **DRF ViewSets**: https://www.django-rest-framework.org/api-guide/viewsets/
- **Django Models**: https://docs.djangoproject.com/en/5.2/topics/db/models/
- **Django Forms**: https://docs.djangoproject.com/en/5.2/topics/forms/

---

**Printed**: March 23, 2026 | **Version**: 1.0
**Keep this handy while developing!**
