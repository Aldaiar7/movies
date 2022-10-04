from django.urls import path, include
from rest_framework.routers import DefaultRouter
from movies.core.api.views.director import DirectorViewSet
from movies.core.api.views.movie import MovieViewSet
from movies.core.api.views.rate import RateViewSet

router = DefaultRouter()

router.register(r'movies', MovieViewSet, basename='movie')
router.register(r'rates', RateViewSet, basename='rate')
router.register(r'directors', DirectorViewSet, basename='director')


app_name = 'api'
urlpatterns = router.urls