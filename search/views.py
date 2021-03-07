from django.shortcuts import render
from .models import Movie, SavedMovie
from django.views.generic import TemplateView, ListView, DetailView
from django.db.models import Q


# def home(request):
  #  return render(request, 'search/home.html')

class HomePageView(TemplateView):
    template_name = 'search/home.html'

class SearchResultsView(ListView):
    model = Movie
    template_name = "search/results.html"
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Movie.objects.filter(Q(title__icontains=query))
        return object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q')        
        return context

class MovieDetailView(DetailView):
    model = Movie
    template_name = "search/movie.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['saved'] = SavedMovie.objects.filter(user_id=self.request.user.id).filter(movie_imdb_id=self.object.pk).exists()
        recommended_movies = self.object.recommendations.split("~")
        context['recommendations'] = Movie.objects.filter(title__in=recommended_movies)[:4]
        return context

# def search(request):
 #   if request.method == 'GET':   
  #      movie_title =  request.GET.get('query')    
   #     try:
    #        status = Movie.objects.filter(title__icontains=movie_title) 
     #       return render(request,"search/results.html", {"movies":status})
      #  except:
       #     return render(request,"search/results.html",{})

