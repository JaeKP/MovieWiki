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


class CharactersSerializer(serializers.ModelSerializer):
    actor_id = ActorSerializer()
    # movie_id = MovieListSerializer()
    class Meta:
        model = Characters
        fields = ('actor_id', 'character_name',)

# 상세 정보용
class MovieSerializer(serializers.ModelSerializer):
    characters_id = CharactersSerializer(many=True, read_only=True)
    production_countries = CountrySerializer(many=True, read_only=True)
    genre_ids = GenreSerializer(many=True, read_only=True)
    director = DirectorSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        # fields = '__all__'
        exclude = ('actors',)

