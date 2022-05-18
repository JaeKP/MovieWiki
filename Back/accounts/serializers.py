from rest_framework import serializers
from movies.serializers.movie import MovieListSerializer
from movies.serializers.movie_review import ProfileMovieReviewSerializer
from articles.serializers.article_comment import ProfileArticleCommentSerializer
from articles.models import Article, ArticleType
from django.contrib.auth import get_user_model
User = get_user_model()

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'nickname', 'profile_image',)

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'nickname', 'region','age', 'profile_image',)

class UserProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('nickname', 'region', 'age', 'profile_image',)

class UserProfileSerializer(serializers.ModelSerializer):
    class ProfileArticleSerializer(serializers.ModelSerializer):
        class ArticleTypeSerializer(serializers.ModelSerializer):
            class Meta:
                model = ArticleType
                fields = ('pk', 'name')
        article_type = ArticleTypeSerializer(read_only=True)
        like_count = serializers.IntegerField(source="like_users.count", read_only=True)

        class Meta:
            model = Article
            fields = ('pk', 'article_type', 'title', 'content', 'created_at', 'article_type','like_count',)
    like_movies = MovieListSerializer(many=True, read_only=True)
    article = ProfileArticleSerializer(many=True, read_only=True)
    comment = ProfileArticleCommentSerializer(many=True, read_only=True)
    review = ProfileMovieReviewSerializer (many=True, read_only=True)
    class Meta:
        model = User
        fields = ('pk', 'nickname', 'region', 'age', 'profile_image','like_movies',  'article',  'comment',  'review',)