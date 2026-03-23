from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Course, Category


@login_required
def dashboard(request):
    if request.user.role == 'instructor':
        # Instructor dashboard
        courses = Course.objects.filter(
            instructor=request.user).select_related('category')
        enrollments = sum(course.enrollments.count() for course in courses)
        context = {
            'courses': courses,
            'total_courses': courses.count(),
            'total_enrollments': enrollments,
            'role': 'instructor'
        }
    else:
        # Student dashboard
        enrollments = request.user.enrollments.select_related('course').all()
        favorites = request.user.favorites.select_related('course').all()
        context = {
            'enrollments': enrollments,
            'favorites': favorites,
            'total_enrollments': enrollments.count(),
            'total_favorites': favorites.count(),
            'role': 'student'
        }
    return render(request, 'courses/dashboard.html', context)


@login_required
def course_list(request):
    courses = Course.objects.filter(
        status='published').select_related('category', 'instructor')
    categories = Category.objects.all()
    return render(request, 'courses/course_list.html', {
        'courses': courses,
        'categories': categories,
    })


@login_required
def course_detail(request, slug):
    course = get_object_or_404(Course, slug=slug, status='published')
    lessons = course.lessons.all()
    is_enrolled = course.enrollments.filter(student=request.user).exists()
    return render(request, 'courses/course_detail.html', {
        'course': course,
        'lessons': lessons,
        'is_enrolled': is_enrolled,
    })


@login_required
def course_create(request):
    if request.user.role != 'instructor':
        messages.error(request, 'Only instructors can create courses.')
        return redirect('courses:dashboard')
    # For now, just redirect to dashboard - full implementation would need forms
    messages.info(request, 'Course creation form would be here.')
    return redirect('courses:dashboard')


@login_required
def course_edit(request, slug):
    course = get_object_or_404(Course, slug=slug, instructor=request.user)
    # For now, just redirect - full implementation would need forms
    messages.info(request, 'Course edit form would be here.')
    return redirect('courses:dashboard')
