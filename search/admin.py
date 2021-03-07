from django.contrib import admin
from .models import Movie, SavedMovie

# Register your models here. 
admin.site.register(Movie)
admin.site.register(SavedMovie)