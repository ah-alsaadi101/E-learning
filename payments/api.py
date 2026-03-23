from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend
from .models import Payment
from . import serializers


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.select_related('student', 'course')
    serializer_class = serializers.PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['student', 'course', 'status', 'payment_method']

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_staff or getattr(self.request.user, 'role', None) == 'admin':
            return queryset
        if getattr(self.request.user, 'role', None) == 'instructor':
            return queryset.filter(course__instructor=self.request.user)
        if self.request.user.role == 'student':
            return queryset.filter(student=self.request.user)
        return queryset.none()

    def perform_create(self, serializer):
        serializer.save(student=self.request.user)
