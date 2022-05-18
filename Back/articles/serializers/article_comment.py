from rest_framework import serializers
from accounts.serializers import UserInfoSerializer
from ..models import ArticleComment


class ArticleCommentSerializer(serializers.ModelSerializer):
    user = UserInfoSerializer(read_only=True)
    like_users = UserInfoSerializer(many=True, read_only=True)
    like_count = serializers.IntegerField(
        source="like_users.count", read_only=True)

    class Meta:
        model = ArticleComment
        fields = ('pk', 'article', 'user', 'content',
                  'created_at', 'like_users', 'like_count')
        read_only_fields = ('article',)
