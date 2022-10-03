# Generated by Django 4.1.1 on 2022-10-03 10:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rate',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_rate', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='moviegenre',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.genre'),
        ),
        migrations.AddField(
            model_name='moviegenre',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.movie'),
        ),
        migrations.AddField(
            model_name='moviecomment',
            name='comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.comment'),
        ),
        migrations.AddField(
            model_name='moviecomment',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.movie'),
        ),
        migrations.AddField(
            model_name='movie',
            name='comment',
            field=models.ManyToManyField(related_name='movie_comments', through='core.MovieComment', to='core.comment'),
        ),
        migrations.AddField(
            model_name='movie',
            name='director',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_director', to='core.director'),
        ),
        migrations.AddField(
            model_name='movie',
            name='genre',
            field=models.ManyToManyField(related_name='movie_genre', through='core.MovieGenre', to='core.genre'),
        ),
        migrations.AddField(
            model_name='movie',
            name='rating',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.rate'),
        ),
        migrations.AddIndex(
            model_name='genre',
            index=models.Index(fields=['name'], name='core_genre_name_ede46a_idx'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_comment', to=settings.AUTH_USER_MODEL),
        ),
    ]
