from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from movies.core.models import Genre
from movies.core.api.serializers.genre import GenreSerializer
from movies.core.api.permissions.permissions import IsSuperUser

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (IsAuthenticated,)

    def get_permissions(self):
        if self.action == 'create' or self.action == 'update' or self.action == 'partial_update' or self.action == 'destroy':
            self.permission_classes = [IsSuperUser]
        return super(self.__class__, self).get_permissions()
