from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from movies.core.api.pagination.pagination import ResultPagination
from movies.core.api.serializers.movie import MovieSerializer, MovieGenreSerializer
from movies.core.models import Movie, MovieGenre
from django_filters.rest_framework import DjangoFilterBackend
from movies.core.api.permissions.permissions import IsSuperUser



class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (IsAuthenticated, )
    pagination_class = ResultPagination
    filter_backends = [DjangoFilterBackend]
    

    def get_permissions(self):
        if self.action == 'create' or self.action == 'update' or self.action == 'partial_update' or self.action == 'destroy':
            self.permission_classes = [IsSuperUser]
        return super(self.__class__, self).get_permissions()

    def get_queryset(self):
        genre = self.request.query_params.get('genre')
        if genre:
            queryset = Movie.objects.filter(genre__name=genre)
            return queryset
        return super().get_queryset()
    


class MovieGenreViewSet(viewsets.ModelViewSet):
    queryset = MovieGenre.objects.all()
    serializer_class = MovieGenreSerializer
    permission_classes = (IsSuperUser, )
    