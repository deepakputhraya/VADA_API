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
		cart.movies.add(movie)
		cart.save()
		return Response(status=200)
	if request.DATA['type']=='game' and request.user.is_authenticated():
		game=Game.objects.get(pk=request.DATA['id'])
		cart=ShoppingCart.objects.get(user=user)
		cart.games.add(game)
		cart.save()
		return Response(status=200)
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