from rest_framework import serializers
from movies.core.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    rating = serializers.IntegerField(read_only=True)
    class Meta:
        model = Movie
        fields = ['id', 'release_date', 'country', 'time', 'age', 'name', 'director', 'rating']
