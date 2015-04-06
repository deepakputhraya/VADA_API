from rest_framework import serializers
from movie.models import Movie,MovieGenre

class MovieGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieGenre
        fields = ('id', 'name')

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title','genre','poster','stock','director','rating','description','releaseDate','language','duration','deposit','rent')
