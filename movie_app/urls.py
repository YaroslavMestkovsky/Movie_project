from . import views
from django.urls import path

urlpatterns = [
    path('', views.show_all_movies),
    path('movie/<slug:slug_movie>', views.show_one_movie, name='movie_detail'),
    path('directors', views.show_directors),
    path('directors/<slug:slug_director>', views.show_one_director, name='one_director'),
    path('actors', views.show_actors),
    path('actors/<slug:slug_actor>', views.show_one_actor, name='one_actor'),
]
