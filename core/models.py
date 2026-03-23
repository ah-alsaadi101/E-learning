from django.db import models


class NewsAndEvents(models.Model):
    POST_TYPE_CHOICES = [
        ('news', 'News'),
        ('event', 'Event'),
    ]

    title = models.CharField(max_length=200)
    summary = models.TextField()
    content = models.TextField(blank=True)
    post_type = models.CharField(
        max_length=10, choices=POST_TYPE_CHOICES, default='news')
    image = models.ImageField(upload_to='news_events/', blank=True, null=True)
    posted_as = models.CharField(
        max_length=20, choices=POST_TYPE_CHOICES, default='news')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'News & Event'
        verbose_name_plural = 'News & Events'
