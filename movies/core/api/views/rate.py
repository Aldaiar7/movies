from rest_framework import viewsets
from movies.core.models import Rate, Movie
from rest_framework.permissions import AllowAny
from movies.core.api.serializers.rate import RateSerializer
from django.db.models import Count


class RateViewSet(viewsets.ModelViewSet):
    """Viewset for Rate model."""
    queryset = Rate.objects.all()
    permission_classes = (AllowAny, )
    serializer_class = RateSerializer
