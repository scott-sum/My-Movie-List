import csv
from search.models import Movie
import django
django.setup()

with open('datasets/final_movies.csv', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader, None)
    for row in reader:
        _, created = Movie.objects.get_or_create(
        imdb_id=row[2],
        title=row[3],
        year=row[4],
        genre=row[5],
        duration=row[6],
        country=row[7],
        director=row[9],
        production_company=row[10],
        actors=row[11],
        description=row[12],
        imdb_url=row[13],
        poster_url=row[14],
        recommendations=row[15])
