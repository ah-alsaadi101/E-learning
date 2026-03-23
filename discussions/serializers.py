from rest_framework import serializers
from .models import Post, Comment


class CommentSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(
        source='author.username', read_only=True)
    author_picture = serializers.ImageField(
        source='author.picture', read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'author', 'author_name', 'author_picture',
                  'content', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


class PostSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(
        source='author.username', read_only=True)
    author_picture = serializers.ImageField(
        source='author.picture', read_only=True)
    course_title = serializers.CharField(source='course.title', read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    comments_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'course', 'course_title', 'author', 'author_name', 'author_picture',
                  'title', 'content', 'comments', 'comments_count', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def get_comments_count(self, obj):
        return obj.comments.count()
