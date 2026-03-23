from django.shortcuts import render
from .models import NewsAndEvents


def news_list(request):
    news = NewsAndEvents.objects.filter(post_type='news')
    return render(request, 'core/news_list.html', {
        'news': news,
        'events_count': NewsAndEvents.objects.filter(post_type='event').count(),
    })


def events_list(request):
    events = NewsAndEvents.objects.filter(post_type='event')
    return render(request, 'core/events_list.html', {'events': events})
