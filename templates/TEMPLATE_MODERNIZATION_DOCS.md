# EduLearn Template Modernization Documentation

## Overview
This document provides comprehensive documentation for the modernized frontend templates in the EduLearn platform. All templates have been updated to extend `base.html`, use Bootstrap 5 components, and include dynamic data binding with Django template syntax.

## Template Structure

### Base Template (`base.html`)
- **Location**: `templates/base.html`
- **Features**:
  - Bootstrap 5.3.0 integration
  - AOS animations
  - Google Fonts (Inter)
  - Responsive navigation
  - Role-based navigation items
  - CSRF token meta tag
  - Custom CSS/JS blocks

### Reusable Components (`templates/components/`)
All components are designed to be included with dynamic data:

#### `course_card.html`
**Usage**: `{% include 'components/course_card.html' with course=course show_enroll=true %}`
**Required Context**:
- `course`: Course model instance
- `show_enroll` (optional): Boolean to show enrollment button
**Features**:
- Course image/thumbnail
- Rating display
- Enrollment status
- Progress indicator
- Instructor info

#### `post_card.html`
**Usage**: `{% include 'components/post_card.html' with post=post show_comments=true %}`
**Required Context**:
- `post`: Discussion post instance
- `show_comments` (optional): Boolean to show comment section
**Features**:
- Author information
- Like/comment counts
- Collapsible comments
- Attachment support

#### `quiz_card.html`
**Usage**: `{% include 'components/quiz_card.html' with quiz=quiz show_take=true %}`
**Required Context**:
- `quiz`: Quiz model instance
- `show_take` (optional): Boolean to show take quiz button
**Features**:
- Quiz statistics
- Attempt tracking
- Passing score display
- Time limit indicator

#### `empty_state.html`
**Usage**: `{% include 'components/empty_state.html' with icon='bi-book' title='No Courses' message='Courses will be available soon' action_url='url_name' action_text='Browse' %}`
**Required Context**:
- `icon`: Bootstrap icon class
- `title`: Main heading
- `message`: Description text
**Optional Context**:
- `action_url`: URL for action button
- `action_text`: Text for action button

#### `loading.html`
**Usage**: `{% include 'components/loading.html' with message='Loading courses...' %}`
**Required Context**:
- `message` (optional): Loading message

## Template Documentation

### Course Templates

#### `course_list.html`
**URL**: `courses:course_list`
**Context Variables**:
```python
{
    'courses': Course.objects.all(),  # Paginated queryset
    'is_paginated': True/False,
    'page_obj': Page object,
    'categories': Category.objects.all(),
    'featured_courses': Course.objects.filter(featured=True)[:3],
    'total_courses': Course.objects.count(),
    'total_students': User.objects.filter(role='student').count(),
    'total_instructors': User.objects.filter(role='instructor').count(),
}
```
**Features**:
- Course filtering by category
- Search functionality
- Featured courses carousel
- Statistics dashboard
- Responsive grid layout

#### `course_detail.html`
**URL**: `courses:course_detail`
**Context Variables**:
```python
{
    'course': Course instance,
    'lessons': course.lessons.all(),
    'enrolled_students': course.enrollments.count(),
    'is_enrolled': user.is_authenticated and course.enrollments.filter(student=user).exists(),
    'progress': enrollment.progress if enrolled else 0,
    'instructor_courses': course.instructor.courses.exclude(id=course.id)[:3],
    'reviews': course.reviews.all(),
    'average_rating': course.reviews.aggregate(Avg('rating'))['rating__avg'],
}
```
**Features**:
- Tabbed interface (Overview, Curriculum, Reviews, Instructor)
- Enrollment status and progress
- Rating system
- Related courses
- Instructor information

### Account Templates

#### `dashboard.html`
**URL**: `accounts:dashboard`
**Context Variables** (varies by role):
```python
# For Students
{
    'enrolled_courses': user.enrollments.all(),
    'completed_courses': user.enrollments.filter(progress=100),
    'total_spent': user.payments.aggregate(Sum('amount'))['amount__sum'],
    'certificates': user.certificates.all(),
    'recent_activity': user.activities.order_by('-created_at')[:5],
}

# For Instructors
{
    'my_courses': user.courses.all(),
    'total_students': user.courses.aggregate(Sum('enrollments__count')),
    'total_earnings': user.payments.aggregate(Sum('amount'))['amount__sum'],
    'course_ratings': user.courses.annotate(avg_rating=Avg('reviews__rating')),
}

# For Admins
{
    'total_users': User.objects.count(),
    'total_courses': Course.objects.count(),
    'total_revenue': Payment.objects.filter(status='completed').aggregate(Sum('amount')),
    'recent_registrations': User.objects.order_by('-date_joined')[:5],
}
```

#### `login.html`
**URL**: `accounts:login`
**Context Variables**:
```python
{
    'form': AuthenticationForm(),
    'next': request.GET.get('next', '/'),
}
```
**Features**:
- CSRF protection
- Remember me option
- Social login placeholders
- Form validation
- Error handling

#### `register.html`
**URL**: `accounts:register`
**Context Variables**:
```python
{
    'form': UserRegistrationForm(),
}
```
**Features**:
- Multi-step registration
- Role selection
- Password strength indicator
- Terms acceptance
- Email verification

#### `profile.html`
**URL**: `accounts:profile`
**Context Variables**:
```python
{
    'user': request.user,
    'enrolled_courses': user.enrollments.all(),
    'completed_courses': user.enrollments.filter(progress=100),
    'certificates': user.certificates.all(),
    'total_spent': user.payments.aggregate(Sum('amount'))['amount__sum'],
    'average_rating': user.reviews.aggregate(Avg('rating'))['rating__avg'],
}
```
**Features**:
- Profile editing
- Course progress tracking
- Achievement badges
- Statistics overview

### Quiz Templates

#### `quiz_list.html`
**URL**: `quizzes:quiz_list`
**Context Variables**:
```python
{
    'quizzes': Quiz.objects.all(),  # Paginated
    'completed_quizzes': user.quiz_attempts.filter(passed=True),
    'average_score': user.quiz_attempts.aggregate(Avg('score'))['score__avg'],
    'certificates_earned': user.certificates.filter(quiz__isnull=False),
}
```

#### `quiz_detail.html`
**URL**: `quizzes:quiz_detail`
**Context Variables**:
```python
{
    'quiz': Quiz instance,
    'user_has_attempted': user.quiz_attempts.filter(quiz=quiz).exists(),
    'user_score': user.quiz_attempts.filter(quiz=quiz).first().score if attempted,
    'user_passed': user.quiz_attempts.filter(quiz=quiz).first().passed if attempted,
    'quiz_attempts': quiz.attempts.all(),
    'passed_attempts': quiz.attempts.filter(passed=True),
    'average_score': quiz.attempts.aggregate(Avg('score'))['score__avg'],
    'highest_score': quiz.attempts.aggregate(Max('score'))['score__max'],
}
```

#### `take_quiz.html`
**URL**: `quizzes:take_quiz`
**Context Variables**:
```python
{
    'quiz': Quiz instance,
    'questions': quiz.questions.order_by('?'),  # Randomized order
}
```
**Features**:
- Real-time timer
- Question navigation
- Progress tracking
- Answer review modal
- Auto-submit on timeout

### Discussion Templates

#### `discussion_list.html`
**URL**: `discussions:discussion_list`
**Context Variables**:
```python
{
    'posts': Post.objects.all(),  # Paginated
    'categories': Category.objects.all(),
    'total_posts': Post.objects.count(),
    'total_comments': Comment.objects.count(),
    'active_users': User.objects.filter(last_login__gte=timezone.now()-timedelta(days=7)),
}
```
**Features**:
- Category filtering
- Search functionality
- Post statistics
- Recent activity
- Modal forms for new posts

### Payment Templates

#### `payment_list.html`
**URL**: `payments:payment_list`
**Context Variables**:
```python
{
    'payments': user.payments.all(),  # Paginated
    'total_spent': user.payments.filter(status='completed').aggregate(Sum('amount'))['amount__sum'],
    'successful_payments': user.payments.filter(status='completed'),
    'pending_payments': user.payments.filter(status='pending'),
    'average_payment': user.payments.filter(status='completed').aggregate(Avg('amount'))['amount__avg'],
}
```
**Features**:
- Payment status indicators
- Receipt downloads
- Transaction history
- Payment method display

### News Templates

#### `news_list.html`
**URL**: `core:news_list`
**Context Variables**:
```python
{
    'news': News.objects.all(),  # Paginated
    'events_count': News.objects.filter(posted_as='Event').count(),
    'total_views': News.objects.aggregate(Sum('views'))['views__sum'],
}
```
**Features**:
- News vs Events distinction
- View counters
- Image thumbnails
- Publication dates

## Testing Guide

### Template Testing Checklist
1. **Base Template Inheritance**: All templates extend `base.html`
2. **Dynamic Data Binding**: All variables are properly referenced
3. **Empty States**: Empty querysets show appropriate messages
4. **Authentication Checks**: User-specific content displays correctly
5. **Role-Based Content**: Admin/Instructor/Student views work
6. **Responsive Design**: Mobile/tablet/desktop layouts
7. **Form Validation**: CSRF tokens and error handling
8. **URL Resolution**: All `{% url %}` tags resolve correctly

### Sample Test Data
```python
# Create test user
user = User.objects.create_user(
    username='testuser',
    email='test@example.com',
    password='testpass123',
    role='student'
)

# Create test course
course = Course.objects.create(
    title='Test Course',
    description='A test course for template testing',
    instructor=user,
    price=99.99,
    category=Category.objects.create(name='Test Category')
)

# Create enrollment
Enrollment.objects.create(
    student=user,
    course=course,
    progress=50
)
```

### View Testing
```python
from django.test import TestCase, Client
from django.contrib.auth import get_user_model

class TemplateTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpass123'
        )

    def test_course_list_template(self):
        response = self.client.get('/courses/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'courses/course_list.html')
        self.assertContains(response, 'Courses')

    def test_authenticated_dashboard(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get('/dashboard/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/dashboard.html')
```

## Development Notes

### Component Usage Patterns
- Always pass required context variables
- Use `{% include %}` with `with` clause for dynamic data
- Components are self-contained with their own styling
- Follow Bootstrap utility classes for responsive design

### Data Binding Best Practices
- Use Django's `|default` filter for optional variables
- Check `user.is_authenticated` before accessing user-specific data
- Use `|length` filter safely with querysets
- Handle `None` values gracefully

### Performance Considerations
- Use `select_related()` and `prefetch_related()` in views
- Paginate large querysets
- Use template caching for expensive operations
- Optimize image loading with proper sizing

### Security Checklist
- All forms include `{% csrf_token %}`
- User input is properly escaped
- Authentication checks before sensitive operations
- Role-based permissions enforced
- XSS prevention through template auto-escaping

## Future Enhancements

### Planned Features
1. **Real-time Updates**: WebSocket integration for live discussions
2. **Advanced Search**: Elasticsearch integration
3. **API Integration**: RESTful endpoints for dynamic content
4. **Progressive Web App**: Service worker and offline capabilities
5. **Accessibility**: WCAG 2.1 compliance improvements

### Component Extensions
- Add more specialized components (calendar, charts, etc.)
- Implement component variants for different use cases
- Create theme customization options

### Performance Optimizations
- Implement lazy loading for images
- Add CDN integration for static files
- Optimize database queries with caching
- Implement HTTP/2 server push

This documentation should be updated as new templates are added or existing ones are modified.