from django.urls import path
from . import views

app_name = 'payments'

urlpatterns = [
    path('course/<int:course_id>/create/', views.create_payment, name='create_payment'),
    path('<int:payment_id>/', views.payment_detail, name='payment_detail'),
    path('', views.payment_list, name='payment_list'),
]
