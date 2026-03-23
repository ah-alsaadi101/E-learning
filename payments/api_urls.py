from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import api

router = DefaultRouter()
router.register(r'payments', api.PaymentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
