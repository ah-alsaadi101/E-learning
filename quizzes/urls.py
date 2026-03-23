from django.urls import path
from . import views

app_name = 'quizzes'

urlpatterns = [
    path('', views.quiz_list, name='quiz_list'),
    path('<slug:slug>/', views.quiz_detail, name='quiz_detail'),
    path('<slug:slug>/take/', views.take_quiz, name='take_quiz'),
]
