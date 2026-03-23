from django.urls import path
from . import views

app_name = 'discussions'

urlpatterns = [
    path('course/<int:course_id>/', views.discussion_list, name='discussion_list'),
    path('course/<int:course_id>/create/', views.create_post, name='create_post'),
    path('post/<int:post_id>/comment/', views.add_comment, name='add_comment'),
]
