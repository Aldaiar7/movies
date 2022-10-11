from rest_framework import serializers
from movies.core.models import Director



class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'
