from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


@api_view(['GET'])
@permission_classes([AllowAny])
def api_root(request):
    return Response({
        'name': 'Merged E-Learning API',
        'health': request.build_absolute_uri('/api/health/'),
        'accounts': request.build_absolute_uri('/api/accounts/users/'),
        'courses': request.build_absolute_uri('/api/courses/courses/'),
        'categories': request.build_absolute_uri('/api/courses/categories/'),
        'lessons': request.build_absolute_uri('/api/courses/lessons/'),
        'enrollments': request.build_absolute_uri('/api/courses/enrollments/'),
        'favorites': request.build_absolute_uri('/api/courses/favorites/'),
        'quizzes': request.build_absolute_uri('/api/quizzes/quizzes/'),
        'questions': request.build_absolute_uri('/api/quizzes/questions/'),
        'attempts': request.build_absolute_uri('/api/quizzes/attempts/'),
        'payments': request.build_absolute_uri('/api/payments/payments/'),
        'posts': request.build_absolute_uri('/api/discussions/posts/'),
        'comments': request.build_absolute_uri('/api/discussions/comments/'),
        'news_events': request.build_absolute_uri('/api/core/news-events/'),
        'auth_examples': {
            'register': request.build_absolute_uri('/api/accounts/users/register/'),
            'login': request.build_absolute_uri('/api/accounts/users/login/'),
            'profile': request.build_absolute_uri('/api/accounts/users/profile/'),
            'logout': request.build_absolute_uri('/api/accounts/users/logout/'),
        },
        'token_header': 'Authorization: Token <your-token>',
    })


@api_view(['GET'])
@permission_classes([AllowAny])
def health_check(request):
    return Response({
        'status': 'ok',
        'service': 'merged-elearning',
    })
