from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='courses:course_list'), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('register/', views.register, name='register'),
]
