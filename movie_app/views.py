from django.shortcuts import render, get_object_or_404
from django.db.models import F, Sum, Max, Min, Count, Avg
# Create your views here.
from .models import Movie


def show_all_movies(request):
    movies = Movie.objects.order_by(F('year').asc(nulls_last=True))
    for movie in movies:
        movie.save()

    movies_info = movies.aggregate(Avg('budget'), Avg('rating'), Min('rating'), Max('rating'), Count('id'))
    return render(request, 'movie_app/all_movies.html', {
        'movies': movies,
        'movies_info': movies_info,
    })


def show_one_movie(request, slug_movie: int):
    movie = get_object_or_404(Movie, slug=slug_movie)
    return render(request, 'movie_app/one_movie.html', {
        'movie': movie
    })
