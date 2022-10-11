from django.urls import path, include
from rest_framework.routers import DefaultRouter
from movies.core.api.views.comment import CommentViewSet
from movies.core.api.views.director import DirectorViewSet
from movies.core.api.views.file import MovieFileViewSet
from movies.core.api.views.movie import MovieGenreViewSet, MovieViewSet
from movies.core.api.views.rate import RateViewSet
from movies.core.api.views.genre import GenreViewSet
from movies.users.api.views.users import UserViewSet


router = DefaultRouter()

router.register(r'movies', MovieViewSet, basename='movie')
router.register(r'rates', RateViewSet, basename='rate')
router.register(r'directors', DirectorViewSet, basename='director')
router.register(r'comments', CommentViewSet, basename='comment')
router.register(r'genres', GenreViewSet, basename='genre')
router.register(r'moviegenres', MovieGenreViewSet, basename='movie_genre')
router.register(r'movie-files', MovieFileViewSet, basename='movie_files')
router.register(r'users', UserViewSet, basename='users')


app_name = 'api'
urlpatterns = router.urls