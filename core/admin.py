from django.contrib import admin
from .models import NewsAndEvents


@admin.register(NewsAndEvents)
class NewsAndEventsAdmin(admin.ModelAdmin):
    list_display = ('title', 'post_type', 'posted_as', 'created_at')
    list_filter = ('post_type', 'posted_as', 'created_at')
    search_fields = ('title', 'summary', 'content')
    readonly_fields = ('created_at', 'updated_at')
