from rest_framework import serializers
from movies.core.models import MovieFile



class MovieFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieFile
        fields = '__all__'
