from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from search.models import SavedMovie, Movie
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
from io import StringIO
import operator

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'user/profile.html', context)

@login_required
def add_saved_movie(request, imdb_id):
    movie = SavedMovie.create(user_id=request.user.id, movie_imdb_id=imdb_id)
    movie.save()
    return redirect('my_movies')

@login_required
def delete_saved_movie(request, imdb_id):
    movie = SavedMovie.objects.get(user_id=request.user.id, movie_imdb_id=imdb_id)
    movie.delete()
    return redirect('my_movies')

@login_required
def my_movies(request):
    savedMovies = SavedMovie.objects.filter(user_id=request.user.id)
    ImdbIds = []
    for savedMovie in savedMovies:
        ImdbIds.append(savedMovie.movie_imdb_id)
    movies = Movie.objects.filter(imdb_id__in=ImdbIds)
    myMovies = zip(savedMovies, movies)
    context = {
        'myMovies': myMovies,
    }
    return render(request, 'user/my_movies.html', context)

def genre_graph(savedMovies):
    genreDict = {}
    for savedMovie in savedMovies:
        movie = Movie.objects.get(imdb_id=savedMovie.movie_imdb_id)
        genres = movie.genre.split(",")
        for genre in genres:
            capitalized_genre = genre.strip().capitalize()
            if capitalized_genre in genreDict:
                genreDict[capitalized_genre] += 1
            else:
                genreDict[capitalized_genre] = 1
    fig = plt.figure()
    plt.barh(list(genreDict.keys()), genreDict.values(), align='center', color='purple')
    plt.title("Your Movie Genres",color='w')
    plt.xlabel("Number of Movies", color='w')
    plt.ylabel("Genre", color='w')
    plt.setp(plt.gca().get_xticklabels(), color="white")
    plt.setp(plt.gca().get_yticklabels(), color="white")
    plt.tick_params(axis='x', colors='white')
    plt.gca().spines['bottom'].set_color('white')
    imgdata = StringIO()
    fig.savefig(imgdata, format='svg', transparent=True)
    imgdata.seek(0)
    return imgdata.getvalue()

def top_movies(allSavedMovies, limit):
    movie_counts = {}
    for movie in allSavedMovies:
        imdb_id = movie.movie_imdb_id
        if imdb_id in movie_counts:
            movie_counts[imdb_id] += 1
        else:
            movie_counts[imdb_id] = 1
    reverse_sorted_movie_counts = dict(sorted(movie_counts.items(), key=operator.itemgetter(1), reverse=True))
    top_movie_dict = list(reverse_sorted_movie_counts)[:limit]
    top_movies = []
    for movie_id in top_movie_dict:
        movie = Movie.objects.get(imdb_id=movie_id)
        top_movies.append(movie)
    return top_movies


@login_required
def statistics(request):
    context = {}
    savedMovies = SavedMovie.objects.filter(user_id=request.user.id)
    allSavedMovies = SavedMovie.objects.all()
    context['genre_graph'] = genre_graph(savedMovies)
    context['top_movies'] = top_movies(allSavedMovies, 5)
    plt.close()
    return render(request, 'user/statistics.html', context)







