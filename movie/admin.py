from django.contrib import admin
from movie.models import Movie,MovieGenre

class MovieGenreAdmin(admin.ModelAdmin):
    list_display = ('name',)

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title','poster',)

admin.site.register(Movie,MovieAdmin)
admin.site.register(MovieGenre,MovieGenreAdmin)
