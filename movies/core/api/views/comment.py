from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from movies.core.api.permissions.permissions import IsSuperUser, IsOwner
from movies.core.models import Comment
from movies.core.api.serializers.comment import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = CommentSerializer

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [IsSuperUser | IsAuthenticated]
        if self.action == 'update' or self.action == 'partial_update':
            self.permission_classes = [IsSuperUser | IsOwner]
        if self.action == 'destroy':
            self.permission_classes = [IsSuperUser | IsOwner]
        return super(self.__class__, self).get_permissions()