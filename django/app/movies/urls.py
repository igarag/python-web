# app/movies/urls.py

from django.urls import path

from .views import MovieList


urlpatterns = [
    path("api/movies/", MovieList.as_view()),
]