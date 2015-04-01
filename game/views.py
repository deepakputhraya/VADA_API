from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from game.serializers import GameSerializer,GameGenreSerializer
from game.models import Game,GameGenre

class GameView(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class GameGenreView(generics.ListCreateAPIView):
    queryset = GameGenre.objects.all()
    serializer_class=GameGenreSerializer

@api_view(['GET'])
def gameDetails(request,pk):
	try:
		game = Game.objects.get(pk=pk)
	except game.DoesNotExist:
		return HttpResponse(status=404)
	if request.method == 'GET':
		serializer = GameSerializer(game)
		return Response(serializer.data)