from rest_framework import serializers
from .models import City

class CitySerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = City
        fields = ('name', 'population', 'photo', 'owner',\
        'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')
