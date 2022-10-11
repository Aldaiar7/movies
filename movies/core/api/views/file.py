from rest_framework import viewsets
from movies.core.api.serializers.file import MovieFileSerializer
from movies.core.models import MovieFile


class MovieFileViewSet(viewsets.ModelViewSet):
    queryset = MovieFile.objects.all()
    serializer_class = MovieFileSerializer
    