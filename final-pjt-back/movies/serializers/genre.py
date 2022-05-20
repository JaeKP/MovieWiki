from rest_framework import serializers
from ..models import Genres

class GenreSerializer(serializers.ModelSerializer):

        class Meta:
            model = Genres
            fields = ('name',)