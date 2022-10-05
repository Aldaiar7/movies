from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from movies.core.models import Comment
from movies.core.api.serializers.comment import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = CommentSerializer
