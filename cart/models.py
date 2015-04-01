from django.db import models
from movie.models import Movie
from game.models import Game
from django.contrib.auth.models import User

class ShoppingCart(models.Model):
	user= models.OneToOneField(User)
	movies = models.ManyToManyField(Movie,null=True,blank=True,default=None)
	games = models.ManyToManyField(Game,null=True,blank=True,default=None)
	time= models.DateTimeField(auto_now=True)