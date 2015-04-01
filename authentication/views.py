from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework import generics
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from authentication.serializers import UserSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from django.contrib import auth
from rest_framework.response import Response
from rest_framework import status
from authentication.models import UserProfile
from cart.models import ShoppingCart
import json


@csrf_exempt
class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer


@api_view(['POST'])
@csrf_exempt
def create_auth(request):
	serialized = UserSerializer(data=request.DATA)
	if serialized.is_valid():
		#return HttpResponse(request.DATA['password'])
		user=User.objects.create_user(
			email=request.DATA['email'],
			password=request.DATA['password'],
			username=request.DATA['username'],
			first_name=request.DATA['first_name'],
			last_name=request.DATA['last_name']
			)
		userProfile=UserProfile(user=user)
		userProfile.save()
		cart=ShoppingCart(user=user)
		cart.save()
		return Response(status=status.HTTP_201_CREATED)
	else:
		return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@csrf_exempt
def login(request):
	if request.user.is_authenticated():
		return HttpResponse("Okay",status=200)
	else:
		user = auth.authenticate(username=request.DATA['username'], password=request.DATA['password'])
		#user = auth.authenticate(username=request.DATA['username'], password=request.DATA['password'])
		if user is not None and user.is_active:
			request.session.set_expiry(0)
			auth.login(request, user)
			response=HttpResponse("Logged in "+request.user.get_full_name(),status=200)
			return response
		else:
			return HttpResponse("Here!",status=500)

@csrf_exempt
def logout(request):
	if request.method=='POST':
		if request.user.is_authenticated():
			name=request.user.get_full_name()
			auth.logout(request)
			return HttpResponse("Logged out "+name)

@csrf_exempt
def authenticate(request):
	if request.user.is_authenticated():
		name=request.user.get_full_name()
		return HttpResponse(name)
	else:
		return HttpResponse(status=500)