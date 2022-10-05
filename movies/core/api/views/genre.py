from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from movies.core.models import Genre
from movies.core.api.serializers.genre import GenreSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (AllowAny,)
