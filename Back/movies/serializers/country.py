from rest_framework import serializers
from ..models import ProductionCountry

class CountrySerializer(serializers.ModelSerializer):

        class Meta:
            model = ProductionCountry
            fields = ('name',)