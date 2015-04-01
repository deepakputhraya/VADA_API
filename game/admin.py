from django.contrib import admin
from game.models import Game,GameGenre

class GameGenreAdmin(admin.ModelAdmin):
    list_display = ('name',)

class GameAdmin(admin.ModelAdmin):
    list_display = ('title','poster',)

admin.site.register(Game,GameAdmin)
admin.site.register(GameGenre,GameGenreAdmin)
