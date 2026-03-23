from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth import authenticate
from .models import User
from . import serializers


class IsAdminOrSelf(permissions.BasePermission):
    """
    Custom permission to only allow admins or the user themselves to edit.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return (
            request.user.is_staff
            or getattr(request.user, 'role', None) == 'admin'
            or obj == request.user
        )


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.prefetch_related('enrollments', 'courses')
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminOrSelf]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['role']

    def get_queryset(self):
        queryset = super().get_queryset()
        if not (
            self.request.user.is_staff
            or getattr(self.request.user, 'role', None) == 'admin'
        ):
            # Non-admins can only see their own profile
            return queryset.filter(id=self.request.user.id)
        return queryset

    @action(detail=False, methods=['post'], permission_classes=[permissions.AllowAny])
    def login(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({'error': 'Username and password are required'}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            serializer = self.get_serializer(user)
            return Response({
                'token': token.key,
                'user': serializer.data
            })
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

    @action(detail=False, methods=['post'], permission_classes=[permissions.AllowAny])
    def register(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key,
                'user': serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'])
    def profile(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)

    @action(detail=False, methods=['post'])
    def logout(self, request):
        try:
            request.user.auth_token.delete()
        except:
            pass
        return Response({'message': 'Successfully logged out'})
