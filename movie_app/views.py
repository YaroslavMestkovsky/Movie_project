from django.shortcuts import render, get_object_or_404
from django.db.models import F, Sum, Max, Min, Count, Avg
# Create your views here.
from .models import Movie, Director, Actor


def show_all_movies(request):
    movies = Movie.objects.order_by(F('year').asc(nulls_last=True))
    for movie in movies:
        movie.save()

    movies_info = movies.aggregate(Avg('budget'), Avg('rating'), Min('rating'), Max('rating'), Count('id'))
    return render(request, 'movie_app/all_movies.html', {
        'movies': movies,
        'movies_info': movies_info,
    })


def show_one_movie(request, slug_movie: str):
    movie = get_object_or_404(Movie, slug=slug_movie)
    return render(request, 'movie_app/one_movie.html', {
        'movie': movie
    })

def show_directors(request):
    directors = Director.objects.order_by('first_name', 'last_name', 'director_mail')
    for director in directors:
        director.save()
    return render(request, 'movie_app/directors.html', {
        'directors': directors,
    })

def show_one_director(request, slug_director: str):
    director = get_object_or_404(Director, slug=slug_director)
    return render(request, 'movie_app/show_director.html', {
        'director': director
    })

def show_actors(request):
    actors = Actor.objects.order_by('first_name', 'last_name', 'gender')
    for actor in actors:
        actor.save()
    return render(request, 'movie_app/actors.html', {
        'actors': actors,
    })

def show_one_actor(request, slug_actor: str):
    actor = get_object_or_404(Actor, slug=slug_actor)
    return render(request, 'movie_app/one_actor.html', {
        'actor': actor
    })

