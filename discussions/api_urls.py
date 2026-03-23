from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import api

router = DefaultRouter()
router.register(r'posts', api.PostViewSet)
router.register(r'comments', api.CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
