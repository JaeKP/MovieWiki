from rest_framework import serializers
from ..models import *
from .actor import ActorSerializer
from .genre import GenreSerializer
from .country import CountrySerializer
from .directors import DirectorSerializer

# 카드 컴포넌트용
class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('id', 'title', 'overview', 'poster_path',)


# 상세 정보용
class MovieSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True, read_only=True)
    production_countries = CountrySerializer(many=True, read_only=True)
    genre_ids = GenreSerializer(many=True, read_only=True)
    director = DirectorSerializer(many=True, read_only=True)
    like_count = serializers.IntegerField(source="like_users.count", read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'

# 장르선별용
class MovieGenreListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('id','genre_ids', 'title',)