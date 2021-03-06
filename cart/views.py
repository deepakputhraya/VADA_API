from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework import generics
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from django.contrib import auth
from rest_framework.response import Response
from rest_framework import status
from authentication.models import UserProfile
from movie.models import Movie
from game.models import Game
from cart.models import ShoppingCart
import json
from cart.serializers import CartSerializer
@api_view(['POST'])
@csrf_exempt
def add_cart(request):
	user=request.user;
	if request.DATA['type']=='movie' and request.user.is_authenticated():
		movie=Movie.objects.get(pk=request.DATA['id'])
		cart=ShoppingCart.objects.get(user=user)
		if movie.stock>0:
			movie.stock=movie.stock-1
			movie.save()
			cart.movies.add(movie)
			cart.save()
			return Response(status=200)
		else:
			return Response(status=500)
	if request.DATA['type']=='game' and request.user.is_authenticated():
		game=Game.objects.get(pk=request.DATA['id'])
		cart=ShoppingCart.objects.get(user=user)
		if game.stock>0:
			game.stock=game.stock-1
			game.save()
			cart.games.add(game)
			cart.save()
			return Response(status=200)
		else:
			return Response(status=500)
	#serializer=UserViewSet(serialized)
	return Response(status=500)

@api_view(['POST'])
@csrf_exempt
def get_cart(request):
	user=request.user;
	if 	request.user.is_authenticated():
		cart=ShoppingCart.objects.get(user=user)
		serializer=CartSerializer(cart)
		return Response(serializer.data,status=200)
	#serializer=UserViewSet(serialized)
	return Response(status=500)

@api_view(['POST'])
@csrf_exempt
def remove_cart(request):
	user=request.user;
	if 	request.user.is_authenticated():
		pk=request.DATA['id']
		cart=ShoppingCart.objects.get(user=user)
		serializer=CartSerializer(cart)
		if request.DATA['type'] == 'movie':
			movie=Movie.objects.get(pk=pk)
			movie.stock=movie.stock+1
			movie.save()
			movies=cart.movies
			movie=movies.get(pk=pk)
			print movie
			print movies
			movies.remove(movie)
			cart.save()
		else:
			game=Game.objects.get(pk=pk)
			game.stock=game.stock+1
			game.save()
			games=cart.games
			game=games.get(pk=pk)
			print games
			print game
			games.remove(game)
			cart.save()
		return Response(serializer.data,status=200)
	#serializer=UserViewSet(serialized)
	return Response(status=500)

@api_view(['POST'])
@csrf_exempt
def check_out(request):
	user=request.user;
	if 	request.user.is_authenticated():
		cart=ShoppingCart.objects.get(user=user)
		cart.games=()
		cart.movies=()
		cart.save()
		serializer=CartSerializer(cart)
		return Response(serializer.data,status=200)
	#serializer=UserViewSet(serialized)
	return Response(status=500)