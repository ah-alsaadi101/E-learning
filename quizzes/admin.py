from django.contrib import admin
from .models import Quiz, Question, MCQuestion, Choice, EssayQuestion, QuizAttempt


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('content', 'quiz_list', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('content', 'explanation')

    def quiz_list(self, obj):
        return ", ".join([quiz.title for quiz in obj.quiz.all()])
    quiz_list.short_description = "Quizzes"


@admin.register(MCQuestion)
class MCQuestionAdmin(QuestionAdmin):
    inlines = [ChoiceInline]


@admin.register(EssayQuestion)
class EssayQuestionAdmin(QuestionAdmin):
    pass


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'category',
                    'pass_mark', 'draft', 'created_at')
    list_filter = ('category', 'draft', 'course', 'created_at')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    # Removed filter_horizontal since questions is reverse relation


@admin.register(QuizAttempt)
class QuizAttemptAdmin(admin.ModelAdmin):
    list_display = ('student', 'quiz', 'current_score',
                    'completed', 'start', 'end')
    list_filter = ('completed', 'start', 'quiz')
    search_fields = ('student__username', 'quiz__title')
    readonly_fields = ('start', 'end', 'user_answers')
