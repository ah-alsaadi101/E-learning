from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('', views.course_list, name='course_list'),
    path('course/<slug:slug>/', views.course_detail, name='course_detail'),
    path('course/create/', views.course_create, name='course_create'),
    path('course/<slug:slug>/edit/', views.course_edit, name='course_edit'),
]
