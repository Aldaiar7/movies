from movies.users.models import User
from movies.users.api.serializers.user_register import RegisterSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,) 
    serializer_class = RegisterSerializer
