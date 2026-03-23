from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers
from .models import Quiz, Question, MCQuestion, Choice, EssayQuestion, QuizAttempt


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['id', 'choice', 'correct']


class QuestionSerializer(serializers.ModelSerializer):
    choices = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = ['id', 'quiz', 'content', 'figure', 'explanation', 'choices']

    def get_choices(self, obj):
        if isinstance(obj, MCQuestion):
            return ChoiceSerializer(obj.choices.all(), many=True).data
        try:
            mc_question = obj.mcquestion
        except ObjectDoesNotExist:
            return []
        return ChoiceSerializer(mc_question.choices.all(), many=True).data


class MCQuestionSerializer(QuestionSerializer):
    choices = ChoiceSerializer(many=True)

    class Meta(QuestionSerializer.Meta):
        model = MCQuestion
        fields = QuestionSerializer.Meta.fields + ['choice_order']

    def create(self, validated_data):
        choices_data = validated_data.pop('choices', [])
        question = super().create(validated_data)
        for choice_data in choices_data:
            Choice.objects.create(question=question, **choice_data)
        return question


class EssayQuestionSerializer(QuestionSerializer):
    class Meta(QuestionSerializer.Meta):
        model = EssayQuestion


class QuizSerializer(serializers.ModelSerializer):
    questions_count = serializers.SerializerMethodField()
    course_title = serializers.CharField(source='course.title', read_only=True)

    class Meta:
        model = Quiz
        fields = ['id', 'course', 'course_title', 'title', 'slug', 'description', 'category',
                  'pass_mark', 'random_order', 'answers_at_end', 'exam_paper', 'single_attempt',
                  'draft', 'questions_count', 'created_at', 'updated_at']
        read_only_fields = ['id', 'slug', 'created_at', 'updated_at']

    def get_questions_count(self, obj):
        return obj.questions.count()


class QuizAttemptSerializer(serializers.ModelSerializer):
    student = serializers.HiddenField(default=serializers.CurrentUserDefault())
    student_name = serializers.CharField(
        source='student.username', read_only=True)
    quiz_title = serializers.CharField(source='quiz.title', read_only=True)
    percent_correct = serializers.SerializerMethodField()

    class Meta:
        model = QuizAttempt
        fields = ['id', 'student', 'student_name', 'quiz', 'quiz_title', 'current_score',
                  'percent_correct', 'start', 'end', 'completed']
        read_only_fields = ['id', 'start', 'end', 'completed']

    def get_percent_correct(self, obj):
        return obj.get_percent_correct()
