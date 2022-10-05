from enum import unique
from io import open_code
from random import choices
from django.db import models
from movies.users.models import User
from django.core.validators import FileExtensionValidator


class Comment(models.Model):
    user = models.ForeignKey(User, related_name='user_comment', on_delete=models.CASCADE)
    text = models.TextField()

class Rate(models.Model):
    class Points(models.IntegerChoices):
        one = 1
        two = 2
        three = 3
        four = 4
        five = 5
        six = 6
        seven = 7
        eight = 8
        nine = 9
        ten = 10
    
    user = models.ForeignKey(User, related_name='user_rate', on_delete=models.CASCADE)
    points = models.IntegerField(choices=Points.choices)
    movie = models.ForeignKey('Movie', related_name='movie_rate', on_delete=models.CASCADE)

class Genre(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        indexes = [
            models.Index(fields=['name'])
        ]

class Director(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)


class Movie(models.Model):
    release_date = models.DateTimeField()
    country = models.CharField(max_length=255)
    director = models.ForeignKey('Director', related_name='movie_director', on_delete=models.CASCADE, null=True)
    time = models.IntegerField()
    age = models.IntegerField()
    name = models.CharField(max_length=255)
    rating = models.IntegerField(null=True)
    comment = models.ManyToManyField('Comment', related_name='movie_comments', through='MovieComment')
    genre = models.ManyToManyField('Genre', related_name='movie_genre', through='MovieGenre')
    cover = models.FileField(upload_to='covers', validators=[FileExtensionValidator(allowed_extensions=['png', 'jpeg', 'jpg'])], null=True)

    class Meta:
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['country']),
            models.Index(fields=['age'])
        ]


class MovieComment(models.Model):
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)
    comment = models.ForeignKey('Comment', on_delete=models.CASCADE)


class MovieGenre(models.Model):
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE)



class MovieFile(models.Model):
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)
    file = models.FileField(upload_to='movies', validators=[FileExtensionValidator(allowed_extensions=['mov', 'mp4'])])
