from movies.core.models import Rate
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Avg
from movies.core.models import Movie

@receiver(post_save, sender=Rate)
def update_movie_rating(sender, instance, created, **kwargs):
    if created:
        movie = instance.movie
        rates = movie.movie_rate.all()
        avg_rate = 0
        for r in rates:
            avg_rate += r.points
        movie.rating = avg_rate // movie.movie_rate.count()
        movie.save(update_fields=['rating'])
