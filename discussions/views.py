from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from courses.models import Course
from .models import Post


@login_required
def discussion_list(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    posts = Post.objects.filter(course=course).select_related(
        'author').prefetch_related('comments')
    return render(request, 'discussions/discussion_list.html', {
        'course': course,
        'posts': posts,
    })
