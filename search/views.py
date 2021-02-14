from django.shortcuts import render
from .models import Movie

def home(request):
    return render(request, 'search/home.html')

def search(request):
    if request.method == 'GET':   
        movie_title =  request.GET.get('query')    
        try:
            status = Movie.objects.filter(title__icontains=movie_title) 
            return render(request,"search/results.html", {"movies":status})
        except:
            return render(request,"search/results.html",{})

