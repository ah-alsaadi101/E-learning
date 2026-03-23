from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import api

router = DefaultRouter()
router.register(r'quizzes', api.QuizViewSet)
router.register(r'questions', api.QuestionViewSet)
router.register(r'attempts', api.QuizAttemptViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
