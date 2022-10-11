from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from movies.users.models import User
from movies.users.api.serializers.users import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def me(self, request):
        queryset = User.objects.filter(pk=request.user.id).first()
        serializer = self.get_serializer(queryset)
        return Response({"user": serializer.data})
