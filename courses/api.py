from rest_framework import viewsets, permissions
from rest_framework.exceptions import PermissionDenied
from django_filters.rest_framework import DjangoFilterBackend
from .models import Category, Course, Lesson, Enrollment, Favorite
from . import serializers


class IsInstructorOrAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated and (
            request.user.is_staff
            or getattr(request.user, 'role', None) in {'instructor', 'admin'}
        )

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user.is_staff or getattr(request.user, 'role', None) == 'admin':
            return True

        course = getattr(obj, 'course', obj)
        return getattr(course, 'instructor', None) == request.user


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = [IsInstructorOrAdminOrReadOnly]


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.select_related('category', 'instructor')
    serializer_class = serializers.CourseSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'instructor', 'status']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsInstructorOrAdminOrReadOnly]

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.query_params.get('category')
        if category:
            queryset = queryset.filter(category__name=category)
        return queryset

    def perform_create(self, serializer):
        serializer.save(instructor=self.request.user)


class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.select_related('course', 'course__instructor')
    serializer_class = serializers.LessonSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['course']
    permission_classes = [permissions.IsAuthenticated, IsInstructorOrAdminOrReadOnly]

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        if user.is_staff or getattr(user, 'role', None) == 'admin':
            return queryset
        if getattr(user, 'role', None) == 'instructor':
            return queryset.filter(course__instructor=user)
        return queryset.filter(course__enrollments__student=user).distinct()

    def perform_create(self, serializer):
        course = serializer.validated_data['course']
        user = self.request.user
        if not (
            user.is_staff
            or getattr(user, 'role', None) == 'admin'
            or course.instructor == user
        ):
            raise PermissionDenied('You can only add lessons to your own courses.')
        serializer.save()


class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = serializers.EnrollmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(student=self.request.user)

    def perform_create(self, serializer):
        serializer.save(student=self.request.user)


class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = serializers.FavoriteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(student=self.request.user)

    def perform_create(self, serializer):
        serializer.save(student=self.request.user)
