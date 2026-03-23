from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Sum
from django.shortcuts import get_object_or_404, redirect, render

from .models import Category, Course, Enrollment


@login_required
def dashboard(request):
    if request.user.role == 'instructor':
        # Instructor dashboard
        courses = Course.objects.filter(
            instructor=request.user).select_related('category')
        enrollments = sum(course.enrollments.count() for course in courses)
        context = {
            'courses': courses,
            'courses_created': courses,
            'total_courses': courses.count(),
            'total_enrollments': enrollments,
            'total_students': Enrollment.objects.filter(
                course__in=courses
            ).values('student').distinct().count(),
            'average_rating': 0,
            'completion_rate': 0,
            'total_revenue': request.user.courses.aggregate(
                total=Sum('payments__amount')
            )['total'] or 0,
            'role': 'instructor'
        }
    else:
        # Student dashboard
        enrollments = request.user.enrollments.select_related('course').all()
        favorites = request.user.favorites.select_related('course').all()
        completed_courses = enrollments.filter(status='completed')
        context = {
            'enrollments': enrollments,
            'enrolled_courses': enrollments,
            'completed_courses': completed_courses,
            'favorites': favorites,
            'total_enrollments': enrollments.count(),
            'total_favorites': favorites.count(),
            'certificates_earned': [],
            'total_points': int(sum(
                enrollment.grade_point or 0 for enrollment in completed_courses
            )),
            'recent_activities': [],
            'upcoming_deadlines': [],
            'recent_achievements': [],
            'role': 'student'
        }
    return render(request, 'courses/dashboard.html', context)


@login_required
def course_list(request):
    courses = Course.objects.filter(
        status='published').select_related('category', 'instructor')
    query = request.GET.get('q', '').strip()
    category = request.GET.get('category', '').strip()
    if query:
        courses = courses.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )
    if category:
        courses = courses.filter(category_id=category)
    categories = Category.objects.all()
    enrolled_course_ids = set(
        request.user.enrollments.values_list('course_id', flat=True)
    )
    return render(request, 'courses/course_list.html', {
        'courses': courses,
        'categories': categories,
        'enrolled_course_ids': enrolled_course_ids,
    })


@login_required
def course_detail(request, slug):
    course = get_object_or_404(
        Course.objects.select_related('category', 'instructor').prefetch_related(
            'lessons', 'posts__author', 'posts__comments__author'
        ),
        slug=slug,
        status='published',
    )
    lessons = course.lessons.all()
    enrollment = course.enrollments.filter(student=request.user).first()
    return render(request, 'courses/course_detail.html', {
        'course': course,
        'lessons': lessons,
        'enrollment': enrollment,
        'is_enrolled': enrollment is not None,
        'recent_posts': course.posts.select_related('author').prefetch_related('comments__author')[:3],
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


@login_required
def enroll(request, course_id):
    course = get_object_or_404(Course, id=course_id, status='published')
    if request.method != 'POST':
        return redirect('courses:course_detail', slug=course.slug)

    if request.user.role != 'student':
        messages.error(request, 'Only students can enroll in courses.')
        return redirect('courses:course_detail', slug=course.slug)

    if course.price > 0:
        from payments.models import Payment

        if not Payment.objects.filter(
            student=request.user,
            course=course,
            status='completed',
        ).exists():
            messages.error(
                request,
                'Please complete payment before enrolling in this course.',
            )
            return redirect('courses:course_detail', slug=course.slug)

    enrollment, created = Enrollment.objects.get_or_create(
        student=request.user,
        course=course,
    )
    if created:
        messages.success(request, 'You have been enrolled successfully.')
    else:
        messages.info(request, 'You are already enrolled in this course.')

    return redirect('courses:course_detail', slug=course.slug)
