from rest_framework import serializers
from .models import NewsAndEvents


class NewsAndEventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsAndEvents
        fields = ['id', 'title', 'summary', 'content', 'post_type', 'image',
                  'posted_as', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
