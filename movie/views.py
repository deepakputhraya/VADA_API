from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from movie.serializers import MovieSerializer,MovieGenreSerializer
from movie.models import Movie,MovieGenre

class MovieView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieGenreView(generics.ListCreateAPIView):
    queryset = MovieGenre.objects.all()
    serializer_class=MovieGenreSerializer

@api_view(['GET'])
def movieDetails(request,pk):
	try:
		movie = Movie.objects.get(pk=pk)
	except Movie.DoesNotExist:
		return HttpResponse(status=404)
	if request.method == 'GET':
		serializer = MovieSerializer(movie)
		return Response(serializer.data)