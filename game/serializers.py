from rest_framework import serializers
from game.models import Game,GameGenre

class GameGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameGenre
        fields = ('id', 'name')

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'title','genre','poster','developer','rating','description','releaseDate')
