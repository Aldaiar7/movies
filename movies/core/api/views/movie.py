from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from movies.core.api.serializers.movie import MovieSerializer
from movies.core.models import Movie



class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (AllowAny, )
 
