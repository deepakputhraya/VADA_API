from rest_framework import serializers
from cart.models import ShoppingCart
from movie.serializers import MovieSerializer
from game.serializers import GameSerializer


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingCart
        movies = MovieSerializer(many=True)
        games = GameSerializer(many=True)
        fields = ('time', 'movies','games')