from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import api

router = DefaultRouter()
router.register(r'categories', api.CategoryViewSet)
router.register(r'courses', api.CourseViewSet)
router.register(r'lessons', api.LessonViewSet)
router.register(r'enrollments', api.EnrollmentViewSet)
router.register(r'favorites', api.FavoriteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
