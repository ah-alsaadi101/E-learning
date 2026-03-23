from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('news/', views.news_list, name='news_list'),
    path('events/', views.events_list, name='events_list'),
]
