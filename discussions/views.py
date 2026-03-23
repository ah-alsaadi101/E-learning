from datetime import timedelta

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from courses.models import Course
from .models import Comment, Post


@login_required
def discussion_list(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    posts = Post.objects.filter(course=course).select_related(
        'author').prefetch_related('comments__author')
    recent_cutoff = timezone.now() - timedelta(days=7)
    return render(request, 'discussions/discussion_list.html', {
        'course': course,
        'posts': posts,
        'total_comments': Comment.objects.filter(post__course=course).count(),
        'recent_activity': posts.filter(created_at__gte=recent_cutoff).count(),
    })


@login_required
def create_post(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method != 'POST':
        return redirect('discussions:discussion_list', course_id=course.id)

    title = request.POST.get('title', '').strip()
    content = request.POST.get('content', '').strip()
    if not title or not content:
        messages.error(request, 'Both a title and content are required.')
        return redirect('discussions:discussion_list', course_id=course.id)

    Post.objects.create(
        course=course,
        author=request.user,
        title=title,
        content=content,
    )
    messages.success(request, 'Your discussion has been posted.')
    return redirect('discussions:discussion_list', course_id=course.id)


@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post.objects.select_related('course'), id=post_id)
    if request.method != 'POST':
        return redirect('discussions:discussion_list', course_id=post.course_id)

    content = request.POST.get('content', '').strip()
    if not content:
        messages.error(request, 'Comment content cannot be empty.')
        return redirect('discussions:discussion_list', course_id=post.course_id)

    Comment.objects.create(
        post=post,
        author=request.user,
        content=content,
    )
    messages.success(request, 'Your comment has been added.')
    return redirect('discussions:discussion_list', course_id=post.course_id)
