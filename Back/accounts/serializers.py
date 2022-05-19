from rest_framework import serializers
from articles.models import Article, ArticleComment, ArticleType
from movies.models import MovieReview, Movie
from django.contrib.auth import get_user_model
User = get_user_model()

# 유저 information 
class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','nickname', 'profile_image',)

# 회원가입 
class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'nickname', 'region','age', 'profile_image',)

# 회원 정보 수정
class UserProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('nickname', 'region', 'age', 'profile_image',)

# 프로필 페이지 
class UserProfileSerializer(serializers.ModelSerializer):
    # movie 시리얼라이저
    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('pk', 'title', 'poster_path',)

    # article 시리얼라이저
    class ArticleSerializer(serializers.ModelSerializer):
        class ArticleTypeSerializer(serializers.ModelSerializer):
            class Meta:
                model = ArticleType
                fields = ('pk', 'name')
        article_type = ArticleTypeSerializer(read_only=True)
        like_count = serializers.IntegerField(source="like_users.count", read_only=True)
        class Meta:
            model = Article
            fields = ('pk', 'article_type', 'title', 'content', 'created_at', 'article_type','like_count',)
    
    # article comment 시리얼라이저
    class ArticleCommentSerializer(serializers.ModelSerializer):
        like_count = serializers.IntegerField(source="like_users.count", read_only=True)
        class Meta: 
            model = ArticleComment
            fields = ('content', 'like_users', 'created_at',)

    # movie review 시리얼라이저
    class MovieReviewSerializer(serializers.ModelSerializer):
        class MovieSerializer(serializers.ModelSerializer):
            class Meta:
                model = Movie
                fields = ('pk', 'title', 'poster_path',)

        movie_id = MovieSerializer(read_only=True)
        like_count = serializers.IntegerField(source="like_users.count", read_only=True)
        class Meta: 
            model = MovieReview
            fields = ('pk','movie_id', 'content', 'spoiler', 'created_at', 'like_count',)


    like_movies = MovieSerializer(many=True, read_only=True)
    article = ArticleSerializer(many=True, read_only=True)
    comment = ArticleCommentSerializer(many=True, read_only=True)
    review = MovieReviewSerializer (many=True, read_only=True)
    class Meta:
        model = User
        fields = '__all__'