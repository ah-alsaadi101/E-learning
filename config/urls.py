"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('courses.urls')),  # Web URLs
    path('accounts/', include('accounts.urls')),
    path('core/', include('core.urls')),
    path('quizzes/', include('quizzes.urls')),
    path('payments/', include('payments.urls')),
    path('discussions/', include('discussions.urls')),
    path('api/', include([
        path('accounts/', include('accounts.api_urls')),
        path('courses/', include('courses.api_urls')),
        path('core/', include('core.api_urls')),
        path('quizzes/', include('quizzes.api_urls')),
        path('payments/', include('payments.api_urls')),
        path('discussions/', include('discussions.api_urls')),
    ])),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
