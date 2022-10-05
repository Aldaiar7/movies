from rest_framework import serializers
from movies.core.models import Movie, MovieGenre


class MovieSerializer(serializers.ModelSerializer):
    rating = serializers.IntegerField(read_only=True)
    class Meta:
        model = Movie
        fields = '__all__'



class MovieGenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = MovieGenre
        fields = '__all__'