from django.urls import path
from . import views
from .views import HomePageView, SearchResultsView, MovieDetailView
from user import views as user_views

urlpatterns = [
    path('', HomePageView.as_view(), name='search-home'),
    path('search/', SearchResultsView.as_view(), name='search-results'),
    path('movie/<pk>/', MovieDetailView.as_view(), name='movie-detail'),
    path('add/<imdb_id>/', user_views.add_saved_movie, name='add-saved-movie'),
    path('delete/<imdb_id>/', user_views.delete_saved_movie, name='delete-saved-movie'),
]