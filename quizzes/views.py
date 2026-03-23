from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Quiz, QuizAttempt


@login_required
def quiz_list(request):
    quizzes = Quiz.objects.filter(draft=False).select_related('course')
    return render(request, 'quizzes/quiz_list.html', {'quizzes': quizzes})


@login_required
def quiz_detail(request, slug):
    quiz = get_object_or_404(Quiz, slug=slug, draft=False)
    return render(request, 'quizzes/quiz_detail.html', {'quiz': quiz})


@login_required
def take_quiz(request, slug):
    quiz = get_object_or_404(Quiz, slug=slug, draft=False)

    # Check if user is enrolled in the course
    if not request.user.enrollments.filter(course=quiz.course).exists():
        messages.error(
            request, 'You must be enrolled in the course to take this quiz.')
        return redirect('quizzes:quiz_detail', slug=slug)

    # Check for existing attempt
    attempt = QuizAttempt.objects.filter(
        student=request.user, quiz=quiz, completed=False).first()
    if not attempt:
        attempt = QuizAttempt.objects.create(student=request.user, quiz=quiz)

    if request.method == 'POST':
        # Handle quiz submission
        attempt.mark_quiz_complete()
        messages.success(
            request, f'Quiz completed! Score: {attempt.get_percent_correct()}%')
        return redirect('quizzes:quiz_detail', slug=slug)

    return render(request, 'quizzes/take_quiz.html', {
        'quiz': quiz,
        'attempt': attempt,
    })
