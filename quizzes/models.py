from django.db import models
from django.conf import settings
from django.utils.text import slugify
from model_utils.managers import InheritanceManager


class Quiz(models.Model):
    CATEGORY_CHOICES = [
        ('assignment', 'Assignment'),
        ('exam', 'Exam'),
        ('practice', 'Practice'),
    ]

    course = models.ForeignKey(
        'courses.Course', on_delete=models.CASCADE, related_name='quizzes')
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(blank=True)
    category = models.CharField(
        max_length=20, choices=CATEGORY_CHOICES, default='practice')
    pass_mark = models.PositiveIntegerField(
        default=50, help_text="Percentage required to pass")
    random_order = models.BooleanField(default=False)
    answers_at_end = models.BooleanField(default=False)
    exam_paper = models.BooleanField(default=False)
    single_attempt = models.BooleanField(default=False)
    draft = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_questions(self):
        return self.questions.all()

    def get_max_score(self):
        return sum(q.get_max_score() for q in self.get_questions())

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']


class Question(models.Model):
    quiz = models.ManyToManyField(Quiz, related_name='questions')
    figure = models.ImageField(upload_to='questions/', blank=True, null=True)
    content = models.TextField()
    explanation = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = InheritanceManager()

    def get_max_score(self):
        return 1  # Default for single question

    def __str__(self):
        return self.content[:50]


class MCQuestion(Question):
    CHOICE_ORDER_CHOICES = [
        ('content', 'Content'),
        ('random', 'Random'),
        ('none', 'None'),
    ]

    choice_order = models.CharField(
        max_length=20, choices=CHOICE_ORDER_CHOICES, default='content')

    def check_if_correct(self, guess):
        answer = Choice.objects.get(id=guess)
        return answer.correct

    def order_choices(self, guess):
        if self.choice_order == 'content':
            return self.get_choices()
        elif self.choice_order == 'random':
            return self.get_choices().order_by('?')
        else:
            return self.get_choices()

    def get_choices(self):
        return self.choices.all()

    def get_choices_list(self):
        return [(choice.id, choice.choice) for choice in self.get_choices()]

    def get_max_score(self):
        return 1


class Choice(models.Model):
    question = models.ForeignKey(
        MCQuestion, on_delete=models.CASCADE, related_name='choices')
    choice = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)

    def __str__(self):
        return self.choice


class EssayQuestion(Question):
    def get_max_score(self):
        return 10  # Arbitrary score for essays


class QuizAttempt(models.Model):
    student = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='quiz_attempts')
    quiz = models.ForeignKey(
        Quiz, on_delete=models.CASCADE, related_name='attempts')
    question_order = models.TextField(
        blank=True)  # Comma-separated question IDs
    question_list = models.TextField(blank=True)   # JSON of questions
    incorrect_questions = models.TextField(blank=True)  # Comma-separated
    current_score = models.IntegerField(default=0)
    user_answers = models.JSONField(default=dict)
    start = models.DateTimeField(auto_now_add=True)
    end = models.DateTimeField(blank=True, null=True)
    completed = models.BooleanField(default=False)

    def get_first_question(self):
        if self.question_order:
            first_id = self.question_order.split(',')[0]
            return Question.objects.get(id=first_id)
        return None

    def remove_first_question(self):
        if self.question_order:
            ids = self.question_order.split(',')
            if ids:
                ids.pop(0)
                self.question_order = ','.join(ids)
                self.save()

    def add_to_score(self, points):
        self.current_score += points
        self.save()

    def get_percent_correct(self):
        total_questions = len(self.question_list.split(
            ',')) if self.question_list else 0
        if total_questions == 0:
            return 0
        return (self.current_score / total_questions) * 100

    def mark_quiz_complete(self):
        self.completed = True
        self.end = models.DateTimeField(auto_now=True)
        self.save()

    def check_if_passed(self):
        return self.get_percent_correct() >= self.quiz.pass_mark

    def result_message(self):
        if self.check_if_passed():
            return "Passed"
        return "Failed"

    def __str__(self):
        return f"{self.student.username} - {self.quiz.title}"

    class Meta:
        ordering = ['-start']
