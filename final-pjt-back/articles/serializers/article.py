from rest_framework import serializers
from ..models import Article
from ..models import ArticleType
from accounts.serializers import UserInfoSerializer
from .article_comment import ArticleCommentSerializer

class ArticleListSerializer(serializers.ModelSerializer):
    class ArticleTypeSerializer(serializers.ModelSerializer):
        class Meta:
            model = ArticleType
            fields = ('pk', 'name')
    article_type = ArticleTypeSerializer()
    user_id = UserInfoSerializer(read_only=True)
    comment_count = serializers.IntegerField(source="comment.count", read_only=True)
    like_count = serializers.IntegerField(source="like_users.count", read_only=True)

    class Meta:
        model = Article
        fields = ('pk', 'article_type', 'user_id','title', 'created_at', 'like_count', 'comment_count')

class ArticleSerializer(serializers.ModelSerializer):
    user_id = UserInfoSerializer(read_only=True)
    comment = ArticleCommentSerializer(many=True, read_only=True)
    like_count = serializers.IntegerField(source="like_users.count", read_only=True)

    class Meta:
        model = Article
        fields = ('pk', 'article_type', 'user_id', 'title', 'content','created_at', 'like_count', 'comment', )

class SearchArticleSerializer(serializers.ModelSerializer):
    class Meta:
            model = Article
            fields = '__all__'