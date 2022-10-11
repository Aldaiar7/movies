from rest_framework import serializers
from movies.users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'username', 'is_superuser', 'is_staff', 'is_active', 'date_joined']
