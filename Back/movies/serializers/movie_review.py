from rest_framework import serializers
from ..models import MovieReview
from .movie import MovieListSerializer

# 프로필용
class ProfileMovieReviewSerializer(serializers.ModelSerializer):
    movie_id = MovieListSerializer(read_only=True)
    like_count = serializers.IntegerField(source="like_users", )
    class Meta: 
        model = MovieReview
        fields = ('pk','movie_id', 'content', 'spoiler', 'create_at', 'like_count',)
