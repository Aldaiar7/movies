from re import L
from rest_framework.generics import ListAPIView
from movies.core.models import Movie
from movies.core.api.serializers.movie import MovieSerializer


class SearchView(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get_queryset(self):
        query = self.request.query_params.get('q')
        return Movie.objects.filter(name__search=query)
