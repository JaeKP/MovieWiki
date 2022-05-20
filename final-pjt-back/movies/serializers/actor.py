from rest_framework import serializers
from ..models import Actor, Movie

class ActorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = ('name', 'profile_path')


class ActorDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = '__all__'