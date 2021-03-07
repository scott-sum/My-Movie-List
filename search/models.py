from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone

# Create your models here.
class Movie(models.Model):
    imdb_id = models.CharField(max_length=30, primary_key=True)
    title = models.CharField(max_length=100)
    year = models.IntegerField()
    genre = models.TextField()
    duration = models.IntegerField()
    country = models.CharField(max_length=30)
    director = models.CharField(max_length=50)
    production_company = models.CharField(max_length=50)
    actors = models.TextField()
    description = models.TextField()
    imdb_url = models.TextField()
    poster_url = models.TextField()
    recommendations = models.TextField()

    def __str__(self):
        return self.title


class SavedMovie(models.Model):
    saved_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    movie_imdb_id = models.CharField(max_length=20)
    date_added = models.DateTimeField()

    @classmethod
    def create(cls, user_id, movie_imdb_id):
        movie = cls(user_id=user_id, movie_imdb_id=movie_imdb_id, date_added=timezone.now())
        return movie
