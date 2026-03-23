from django.urls import path
from . import views

app_name = 'discussions'

urlpatterns = [
    path('course/<int:course_id>/', views.discussion_list, name='discussion_list'),
]
