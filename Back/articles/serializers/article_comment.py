from rest_framework import serializers
from ..models import ArticleComment
from django.contrib.auth import get_user_model

User = get_user_model()


class ArticleCommentSerializer(serializers.ModelSerializer):
    class UserInfoSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'nickname', 'profile_image',)
    user = UserInfoSerializer(read_only=True)
    like_count = serializers.IntegerField(source="like_users.count", read_only=True)

    class Meta:
        model = ArticleComment
        fields = ('pk', 'article', 'user', 'content','created_at', 'like_count')
        read_only_fields = ('article',)


# 유저 프로필용
class ProfileArticleCommentSerializer(serializers.ModelSerializer):
    like_count = serializers.IntegerField(source="like_users.count", read_only=True)
    class Meta:
        model = ArticleComment
        fields = ('pk', 'article', 'content','created_at', 'like_count')