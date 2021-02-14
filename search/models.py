from django.db import models
import csv


# Create your models here.
class Movie(models.Model):
    imdb_id = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    year = models.IntegerField()
    genre = models.TextField()
    duration = models.IntegerField()
    country = models.CharField(max_length=30)
    director = models.CharField(max_length=50)
    production_company = models.CharField(max_length=50)
    actors = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.title
