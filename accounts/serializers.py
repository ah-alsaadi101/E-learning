from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import User

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)
    enrollments_count = serializers.SerializerMethodField()
    courses_count = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name', 'role',
                  'phone', 'address', 'picture', 'bio', 'enrollments_count',
                  'courses_count', 'date_joined', 'last_login']
        read_only_fields = ['id', 'date_joined',
                            'last_login', 'enrollments_count', 'courses_count']

    def get_enrollments_count(self, obj):
        if hasattr(obj, 'enrollments'):
            return obj.enrollments.count()
        return 0

    def get_courses_count(self, obj):
        if hasattr(obj, 'courses'):
            return obj.courses.count()
        return 0

    def validate(self, attrs):
        if self.instance is None and not attrs.get('password'):
            raise serializers.ValidationError(
                {'password': 'This field is required when creating a user.'}
            )
        return attrs

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        return User.objects.create_user(password=password, **validated_data)

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    """Simplified serializer for user profiles in other endpoints"""
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'full_name', 'picture', 'role']

    def get_full_name(self, obj):
        return obj.get_full_name() or obj.username
