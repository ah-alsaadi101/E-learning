# Security & Performance Guide

Complete documentation of all security and performance features implemented in the E-Learning Platform.

## 🔒 Security Features

### 1. Authentication & Authorization

#### Token-Based API Authentication

- Implemented using Django REST Framework tokens
- Each user gets a unique token upon login
- Tokens required for all API operations
- Tokens can be revoked immediately

**How it works:**

```
1. User logs in with username/password
2. Server validates credentials against hashed password
3. Server generates secure token
4. Client sends token in Authorization header
5. Server validates token on each request
```

#### Session-Based Authentication

- Traditional session cookies for web interface
- CSRF tokens prevent cross-site attacks
- Secure session settings in production

#### Password Security

- Minimum 8 characters required
- Complexity requirements enforced
- Hashed with PBKDF2 algorithm (not stored in plain text)
- 100,000 iterations for password hashing
- Users cannot use common passwords (from 20,000 most common)

### 2. CSRF Protection

**What it prevents:** Cross-Site Request Forgery attacks

**How it works:**

- Every form includes CSRF token
- Token verified on form submission
- Tokens tied to session
- Tokens expire after timeout

**Configuration:**

```python
MIDDLEWARE = [
    'django.middleware.csrf.CsrfViewMiddleware',
]
CSRF_COOKIE_SECURE = True  # HTTPS only in production
CSRF_COOKIE_HTTPONLY = False  # Accessible to JavaScript
CSRF_TRUSTED_ORIGINS = ['yourdomain.com']
```

### 3. SQL Injection Prevention

**Django ORM Protection:**

- All database queries use parameterized statements
- Never concatenate user input into SQL
- SQL injection impossible through ORM

**Example (Safe):**

```python
# Safe - Django ORM
Course.objects.filter(title=user_input)

# Dangerous (Don't do this!)
Course.objects.raw(f"SELECT * FROM courses WHERE title = '{user_input}'")
```

### 4. XSS (Cross-Site Scripting) Prevention

**Template Auto-Escaping:**

- All variables automatically HTML-escaped
- Tags protected from injection
- JavaScript payload execution prevented

**Security Headers:**

```python
SECURE_CONTENT_SECURITY_POLICY = {
    'default-src': ("'self'",),
    'script-src': ("'self'", "'unsafe-inline'"),
    'style-src': ("'self'", "'unsafe-inline'"),
}
```

**What this does:**

- Limits script sources to same origin
- Prevents execution of inline scripts
- Protects against injected JavaScript

### 5. HTTP Security Headers

All responses include protective headers:

```
X-Content-Type-Options: nosniff
  └─ Prevents MIME type sniffing

X-Frame-Options: DENY
  └─ Prevents clickjacking

X-XSS-Protection: 1; mode=block
  └─ Enables browser XSS filter

Strict-Transport-Security: max-age=31536000; includeSubDomains
  └─ Forces HTTPS connections

Content-Security-Policy: default-src 'self'
  └─ Restricts resource loading
```

### 6. SSL/TLS Encryption

**In Production:**

```python
SECURE_SSL_REDIRECT = True  # Redirect HTTP → HTTPS
SESSION_COOKIE_SECURE = True  # Only send cookie over HTTPS
CSRF_COOKIE_SECURE = True  # Only send CSRF token over HTTPS
SECURE_HSTS_SECONDS = 31536000  # Force HTTPS for 1 year
```

**Certificate Management:**

- Use Let's Encrypt (automatic renewal)
- Minimum TLS 1.2 required
- Strong cipher suites only

### 7. Rate Limiting

**API Protection:**

```python
# Install: pip install djangorestframework-ratelimit
THROTTLE_RATES = {
    'anon': '100/hour',  # Anonymous users: 100 requests/hour
    'user': '1000/hour',  # Authenticated users: 1000 requests/hour
}
```

**Prevents:**

- Brute force attacks
- DDoS attacks
- API abuse

### 8. File Upload Security

**Validation & Restrictions:**

```python
# Allowed extensions
ALLOWED_EXTENSIONS = ['pdf', 'docx', 'xlsx', 'jpg', 'png']

# File size limits
MAX_FILE_SIZE = 50 * 1024 * 1024  # 50 MB

# File type verification
import magic
file_type = magic.from_buffer(file_content, mime=True)
```

**Storage Security:**

- Files stored outside web root
- Served with `X-Sendfile` (nginx/apache)
- User-uploaded files cannot be executed
- Filenames sanitized to prevent directory traversal

### 9. Input Validation

**Serializer Validation:**

```python
class CourseSerializer(serializers.ModelSerializer):
    def validate_title(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Title too short")
        return value

    def validate(self, data):
        # Cross-field validation
        if data['end_date'] < data['start_date']:
            raise serializers.ValidationError("Invalid date range")
        return data
```

**Database Constraints:**

```python
class User(AbstractUser):
    email = models.EmailField(unique=True)  # Unique constraint
    username = models.CharField(max_length=150, unique=True)
```

### 10. Logging & Audit Trail

**Security Events Logged:**

```python
LOGGING = {
    'handlers': {
        'file': {
            'filename': '/var/log/elearning/security.log',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django.security': {
            'handlers': ['file'],
            'level': 'INFO',
        },
    },
}
```

**Tracked Events:**

- Login attempts (success/failure)
- Permission denied errors
- Admin actions
- Data modifications
- File uploads
- API token usage

### 11. Permission System

**Object-Level Permissions:**

```python
class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
```

**Role-Based Access:**

```python
# Permission checks
if user.role != 'instructor':
    raise PermissionDenied("Only instructors can create courses")
```

**Database-Level:**

- Foreign key constraints prevent orphaned records
- Unique constraints prevent duplicates
- Check constraints enforce business rules

### 12. Secrets Management

**Never commit secrets:**

```env
# .env (NEVER commit this)
SECRET_KEY=your-secret-key
DATABASE_PASSWORD=your-password
EMAIL_PASSWORD=your-email-password
```

**Using Environment Variables:**

```python
SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = os.getenv('DEBUG', 'False') == 'True'
```

### 13. Dependency Security

**Regular Updates:**

```bash
# Check for vulnerabilities
pip-audit

# Update safely
pip install --upgrade django
```

**Lock Versions:**

```
Django==5.2.12  # Specific version (not >=)
djangorestframework==3.15.2
```

---

## ⚡ Performance Features

### 1. Database Query Optimization

**N+1 Query Prevention:**

```python
# Bad (N+1 queries)
courses = Course.objects.all()
for course in courses:
    print(course.instructor.name)  # Database hit for each course!

# Good (single query with join)
courses = Course.objects.select_related('instructor')
for course in courses:
    print(course.instructor.name)  # No additional queries

# For reverse relationships
courses = Course.objects.prefetch_related('lessons', 'enrollments')
```

**Pagination:**

```python
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20,
}
```

**Database Indexing:**

```python
class Course(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(unique=True)  # Unique = indexed
    status = models.CharField(choices=..., db_index=True)
```

### 2. Response Caching

**Page Caching:**

```python
from django.views.decorators.cache import cache_page

@cache_page(3600)  # Cache for 1 hour
def course_list(request):
    ...
```

**Query Result Caching:**

```python
from django.core.cache import cache

def get_course_details(course_id):
    cached = cache.get(f'course_{course_id}')
    if cached:
        return cached

    course = Course.objects.select_related(
        'instructor', 'category'
    ).prefetch_related(
        'lessons'
    ).get(id=course_id)

    cache.set(f'course_{course_id}', course, 3600)
    return course
```

**Cache Configuration:**

```python
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'elearning-cache',
    }
}
```

### 3. Database Connection Pooling

**Persistent Connections:**

```python
DATABASES = {
    'default': {
        'CONN_MAX_AGE': 600,  # Keep connections for 10 minutes
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            'charset': 'utf8mb4',
        }
    }
}
```

### 4. Lazy Loading & Queryset Evaluation

**Smart Evaluation:**

```python
# Evaluated immediately (runs query now)
users = list(User.objects.all())

# Lazy (query runs when iteration)
users = User.objects.all()
for user in users:  # Query runs here
    print(user.name)

# Better (explicit queryset)
users = User.objects.filter(role='student')
# Query runs only when accessed
```

### 5. Field Selection

**Only Fetch Required Fields:**

```python
# Bad - fetches all fields
User.objects.all()

# Good - only needed fields
User.objects.values('id', 'username', 'email')
User.objects.values_list('id', 'username')
```

### 6. Batch Operations

**Bulk Create/Update:**

```python
# Instead of looping:
# for user in users:
#     user.save()

# Use bulk operations:
User.objects.bulk_create(users, batch_size=1000)
User.objects.bulk_update(users, fields=['status'], batch_size=1000)
```

### 7. Serializer Optimization

**Optimized Serializers:**

```python
class CourseSerializer(serializers.ModelSerializer):
    instructor_name = serializers.CharField(
        source='instructor.username',
        read_only=True
    )
    lessons_count = serializers.SerializerMethodField()

    def get_lessons_count(self, obj):
        # Access pre-fetched data
        return obj.lessons.all().count()
```

### 8. Compression & Minification

**GZIP Compression:**

```python
MIDDLEWARE = [
    'django.middleware.gzip.GZipMiddleware',
]
```

**Static File Compression:**

```bash
# Collect and compress
python manage.py collectstatic --compress
```

### 9. Logging Performance

**Efficient Logging:**

```python
import logging
logger = logging.getLogger(__name__)

# Log only important events
logger.info("User enrolled in course")  # Info level
logger.debug("Database query executed")  # Debug level (disabled in production)
```

### 10. Monitoring & Profiling

**Database Query Monitoring:**

```python
from django.test.utils import CaptureQueriesContext
from django.db import connection

with CaptureQueriesContext(connection) as context:
    # Your code here
    courses = Course.objects.select_related('instructor').all()

print(f"Queries: {len(context.captured_queries)}")
for query in context.captured_queries:
    print(query['sql'])
```

**Request Profiling:**

```bash
# Install: pip install django-silk
python manage.py collectstatic
# Visit: /silk/

# Or use Django Debug Toolbar (development only)
# pip install django-debug-toolbar
```

### 11. Async Support

**Future Enhancement (Django 4.1+):**

```python
async def async_view(request):
    courses = await Course.objects.aget(id=1)
    return JsonResponse({'course': str(courses)})
```

### 12. CDN Integration

**Serve Static Files via CDN:**

```python
STATIC_URL = 'https://cdn.yourdomain.com/'
```

**Cache Headers for Static Files:**

```
Cache-Control: public, max-age=31536000, immutable
```

---

## 🔍 Monitoring & Debugging

### Health Check Endpoint

```python
# Add to urls.py
path('health/', HealthCheckView.as_view())
```

### Application Monitoring

**Sentry Integration:**

```python
import sentry_sdk
sentry_sdk.init(
    dsn="https://key@sentry.io/project",
    traces_sample_rate=0.1,
)
```

### Performance Metrics

**Track Key Metrics:**

- Response time (avg, p95, p99)
- Database query count
- Cache hit rate
- Error rate
- User session duration

---

## Production Deployment Checklist

- [ ] All passwords hashed (PBKDF2)
- [ ] DEBUG = False
- [ ] ALLOWED_HOSTS set
- [ ] SECRET_KEY rotated
- [ ] HTTPS enabled
- [ ] Security headers configured
- [ ] CSRF protection enabled
- [ ] SQL injection prevention verified
- [ ] XSS prevention enabled
- [ ] CORS properly configured
- [ ] Rate limiting enabled
- [ ] File upload validation enabled
- [ ] Logging configured
- [ ] Backups scheduled
- [ ] Monitoring enabled
- [ ] Firewall rules set
- [ ] SSH hardened
- [ ] Database backups automated
- [ ] SSL certificate valid
- [ ] Gzip compression enabled

---

## Security & Performance Best Practices

1. **Keep Django Updated**: Security patches released regularly
2. **Monitor Dependencies**: Use `pip-audit` to check for vulnerabilities
3. **Regular Backups**: Daily automated backups to separate location
4. **Log Rotation**: Prevent logs filling disk space
5. **Monitoring**: Track application health and performance
6. **Testing**: Automated tests catch regressions
7. **Code Review**: Review changes before deployment
8. **Principle of Least Privilege**: Users only get needed permissions
9. **Input Validation**: Always validate user input
10. **Output Escaping**: Always escape output in templates

---

**Last Updated**: March 2026
