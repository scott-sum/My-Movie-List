# Generated by Django 3.1.7 on 2021-03-07 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0002_movie_recommendations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='production_company',
            field=models.CharField(max_length=100),
        ),
    ]
