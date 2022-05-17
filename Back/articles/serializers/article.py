from rest_framework import serializers
from django.contrib.auth import get_user_model
from ..models import Article, ArticleType, ArticleComment
from accounts.serializers import UserInfoSerializer

User = get_user_model()

class ArticleListSerializer(serializers.ModelSerializer):
    class ArticleTypeSerializer(serializers.ModelSerializer):
        class Meta:
            model = ArticleType
            fields = ('pk', 'name')

    article_type = ArticleTypeSerializer()
    user_id = UserInfoSerializer(read_only=True)
    like_count = serializers.IntegerField()

    class Meta:
        model = Article
        fields = ('pk','article_type', 'user_id', 'title', 'created_at', 'like_count',)


class ArticleSerializer(serializers.ModelSerializer):
    class ArticleCommentSerializer(serializers.ModelSerializer):
        user = UserInfoSerializer(read_only=True)
        like_users = UserInfoSerializer(many=True, read_only=True)
        like_count = serializers.IntegerField(source="like_users.count", read_only=True)

        class Meta:
            model = ArticleComment
            fields = ('pk', 'user', 'content', 'like_count', 'created_at', 'like_users',)

    user_id = UserInfoSerializer(read_only=True)
    comment = ArticleCommentSerializer(many=True, read_only=True)
    like_users = UserInfoSerializer(many=True, read_only=True)
    like_count = serializers.IntegerField(source="like_users.count", read_only=True)

    class Meta:
        model=Article
        fields=('pk', 'article_type', 'user_id', 'title', 'content','created_at', 'like_count', 'like_users', 'comment', )