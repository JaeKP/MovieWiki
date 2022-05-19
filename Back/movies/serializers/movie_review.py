import re
from rest_framework import serializers
from ..models import MovieReview
from .movie import MovieListSerializer
from django.contrib.auth import get_user_model
User = get_user_model()

# 영화 리뷰 
class MovieReviewSerializer(serializers.ModelSerializer):
    class UserInfoSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('username', 'age', 'nickname', 'profile_image',)
    user_id = UserInfoSerializer(read_only=True)
    like_count = serializers.IntegerField(read_only=True)
    class Meta:
        model = MovieReview
        fields = '__all__'
        read_only_fields = ('movie_id','like_users',)



# 프로필용
class ProfileMovieReviewSerializer(serializers.ModelSerializer):
    movie_id = MovieListSerializer(read_only=True)
    like_count = serializers.IntegerField(source="like_users", read_only=True)
    class Meta: 
        model = MovieReview
        fields = ('pk','movie_id', 'content', 'spoiler', 'create_at', 'like_count',)
