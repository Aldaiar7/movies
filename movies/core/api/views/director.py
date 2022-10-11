from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from movies.core.api.serializers.director import DirectorSerializer
from movies.core.models import Director



class DirectorViewSet(viewsets.ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    permission_classes = (IsAuthenticated,)
