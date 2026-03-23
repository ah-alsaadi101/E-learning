from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404, redirect, render
from .models import Quiz, QuizAttempt


@login_required
def quiz_list(request):
    quizzes = Quiz.objects.filter(draft=False).select_related('course')
    completed_attempts = list(
        request.user.quiz_attempts.filter(completed=True).select_related('quiz')
    )
    average_score = (
        sum(attempt.get_percent_correct() for attempt in completed_attempts) / len(completed_attempts)
        if completed_attempts else 0
    )
    return render(request, 'quizzes/quiz_list.html', {
        'quizzes': quizzes,
        'completed_quizzes': completed_attempts,
        'average_score': average_score,
        'certificates_earned': [],
    })


@login_required
def quiz_detail(request, slug):
    quiz = get_object_or_404(Quiz, slug=slug, draft=False)
    latest_attempt = QuizAttempt.objects.filter(
        student=request.user,
        quiz=quiz,
        completed=True,
    ).order_by('-end').first()
    return render(request, 'quizzes/quiz_detail.html', {
        'quiz': quiz,
        'latest_attempt': latest_attempt,
    })


@login_required
def take_quiz(request, slug):
    quiz = get_object_or_404(Quiz, slug=slug, draft=False)
    questions = quiz.questions.all().prefetch_related('mcquestion__choices')

    # Check if user is enrolled in the course
    if not request.user.enrollments.filter(course=quiz.course).exists():
        messages.error(
            request, 'You must be enrolled in the course to take this quiz.')
        return redirect('quizzes:quiz_detail', slug=slug)

    if quiz.single_attempt and QuizAttempt.objects.filter(
        student=request.user,
        quiz=quiz,
        completed=True,
    ).exists():
        messages.info(request, 'This quiz only allows a single completed attempt.')
        return redirect('quizzes:quiz_detail', slug=slug)

    # Check for existing attempt
    attempt = QuizAttempt.objects.filter(
        student=request.user, quiz=quiz, completed=False).first()
    if not attempt:
        attempt = QuizAttempt.objects.create(student=request.user, quiz=quiz)

    if request.method == 'POST':
        question_ids = []
        answers = {}
        score = 0
        for question in questions:
            question_ids.append(str(question.id))
            answer = request.POST.get(f'question_{question.id}')
            if answer is None or answer == '':
                continue

            answers[str(question.id)] = answer
            try:
                mc_question = question.mcquestion
            except ObjectDoesNotExist:
                mc_question = None

            if mc_question:
                try:
                    if mc_question.check_if_correct(answer):
                        score += mc_question.get_max_score()
                except Exception:
                    continue

        attempt.question_order = ','.join(question_ids)
        attempt.question_list = ','.join(question_ids)
        attempt.user_answers = answers
        attempt.current_score = score
        attempt.mark_quiz_complete()
        messages.success(
            request, f'Quiz completed! Score: {attempt.get_percent_correct()}%')
        return redirect('quizzes:quiz_detail', slug=slug)

    return render(request, 'quizzes/take_quiz.html', {
        'quiz': quiz,
        'attempt': attempt,
        'questions': questions,
    })
