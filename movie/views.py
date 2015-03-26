from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics
from movie.serializers import MovieSerializer,MovieGenreSerializer
from movie.models import Movie,MovieGenre

class MovieView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieGenreView(generics.ListCreateAPIView):
    queryset = MovieGenre.objects.all()
    serializer_class=MovieGenreSerializer
