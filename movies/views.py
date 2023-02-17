from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from django.db.models import Count, F

from movies.models import Movies,Actors,Movies_Actors
from movies.serializers import MoviesSerializer,ActorsSerializer

# Create your views here.
@csrf_exempt
def moviesApi(request):
    if request.method == "GET":
        movies = Movies.objects.annotate(actors_count=Count("movies_actors"))
        movies_serializer = MoviesSerializer(movies, many=True)
        return JsonResponse(movies_serializer.data, safe=False)

@csrf_exempt
def actorsApi(request):
    if request.method == "GET":
        actors = Actors.objects.annotate(movies_count=Count("movies_actors"))
        actors_serializer = ActorsSerializer(actors, many=True)
        return JsonResponse(actors_serializer.data, safe=False)

@csrf_exempt
def addLike(request, id):
    movie = Movies.objects.get(MovieID=id)
    movie.likes += 1
    movie.save()
    return JsonResponse({'likes':str(movie.likes)})

@csrf_exempt
def delLike(request, id):
    movie = Movies.objects.get(MovieID=id)
    movie.likes -= 1
    movie.save()
    return JsonResponse({'likes':str(movie.likes)})