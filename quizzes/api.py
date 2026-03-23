from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Quiz, Question, MCQuestion, EssayQuestion, QuizAttempt
from . import serializers


class IsInstructorOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow instructors to create/edit quizzes.
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.role == 'instructor'

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        course = getattr(obj, 'course', None)
        if course is not None:
            return course.instructor == request.user

        quiz_manager = getattr(obj, 'quiz', None)
        if hasattr(quiz_manager, 'all'):
            return quiz_manager.filter(course__instructor=request.user).exists()

        return False


class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.select_related(
        'course').prefetch_related('questions')
    serializer_class = serializers.QuizSerializer
    permission_classes = [permissions.IsAuthenticated, IsInstructorOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['course', 'category', 'draft']

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.role == 'student':
            # Students can only see published quizzes for courses they're enrolled in
            enrolled_course_ids = self.request.user.enrollments.values_list(
                'course_id', flat=True)
            return queryset.filter(course_id__in=enrolled_course_ids, draft=False)
        return queryset

    @action(detail=True, methods=['post'])
    def start_attempt(self, request, pk=None):
        quiz = self.get_object()
        if QuizAttempt.objects.filter(student=request.user, quiz=quiz, completed=False).exists():
            return Response({'error': 'You already have an active attempt'}, status=status.HTTP_400_BAD_REQUEST)

        attempt = QuizAttempt.objects.create(student=request.user, quiz=quiz)
        serializer = serializers.QuizAttemptSerializer(attempt)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class QuestionViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.QuestionSerializer
    queryset = Question.objects.prefetch_related('quiz', 'mcquestion__choices')
    permission_classes = [permissions.IsAuthenticated, IsInstructorOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['quiz']

    def get_serializer_class(self):
        if hasattr(self.request.data, 'get') and 'choice_order' in self.request.data:
            return serializers.MCQuestionSerializer
        return serializers.QuestionSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        quiz_id = self.request.query_params.get('quiz')
        if quiz_id:
            return queryset.filter(quiz__id=quiz_id).distinct()
        return queryset


class QuizAttemptViewSet(viewsets.ModelViewSet):
    queryset = QuizAttempt.objects.select_related('student', 'quiz')
    serializer_class = serializers.QuizAttemptSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['quiz', 'completed']

    def get_queryset(self):
        return self.queryset.filter(student=self.request.user)

    def perform_create(self, serializer):
        serializer.save(student=self.request.user)

    @action(detail=True, methods=['post'])
    def submit_answer(self, request, pk=None):
        attempt = self.get_object()
        if attempt.completed:
            return Response({'error': 'Quiz attempt is already completed'}, status=status.HTTP_400_BAD_REQUEST)

        question_id = request.data.get('question_id')
        answer = request.data.get('answer')

        if not question_id or answer is None:
            return Response({'error': 'question_id and answer are required'}, status=status.HTTP_400_BAD_REQUEST)

        attempt.user_answers[question_id] = answer
        attempt.save()

        return Response({'message': 'Answer submitted successfully'})

    @action(detail=True, methods=['post'])
    def complete_attempt(self, request, pk=None):
        attempt = self.get_object()
        if attempt.completed:
            return Response({'error': 'Quiz attempt is already completed'}, status=status.HTTP_400_BAD_REQUEST)

        attempt.mark_quiz_complete()
        serializer = self.get_serializer(attempt)
        return Response(serializer.data)
