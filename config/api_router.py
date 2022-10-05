from django.urls import path, include
from rest_framework.routers import DefaultRouter
from movies.core.api.views.comment import CommentViewSet
from movies.core.api.views.director import DirectorViewSet
from movies.core.api.views.movie import MovieGenreViewSet, MovieViewSet
from movies.core.api.views.rate import RateViewSet
from movies.core.api.views.genre import GenreViewSet

router = DefaultRouter()

router.register(r'movies', MovieViewSet, basename='movie')
router.register(r'rates', RateViewSet, basename='rate')
router.register(r'directors', DirectorViewSet, basename='director')
router.register(r'comments', CommentViewSet, basename='comment')
router.register(r'genres', GenreViewSet, basename='genre')
router.register(r'moviegenres', MovieGenreViewSet, basename='movie_genre')


app_name = 'api'
urlpatterns = router.urls