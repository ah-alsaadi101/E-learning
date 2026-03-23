from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend
from .models import NewsAndEvents
from . import serializers


class NewsAndEventsViewSet(viewsets.ModelViewSet):
    queryset = NewsAndEvents.objects.all()
    serializer_class = serializers.NewsAndEventsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['post_type', 'posted_as']

    def get_queryset(self):
        queryset = super().get_queryset()
        post_type = self.request.query_params.get('type')
        if post_type:
            queryset = queryset.filter(post_type=post_type)
        return queryset.order_by('-created_at')
