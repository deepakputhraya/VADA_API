from django.conf.urls import patterns, include, url
from django.contrib import admin
from movie.views import MovieView,MovieGenreView,movieDetails
from game.views import GameView,GameGenreView,gameDetails
from authentication import views
from django.conf import settings
from rest_framework import routers
from authentication.views import UserViewSet,login,logout,authenticate,create_auth
from cart.views import add_cart,get_cart,remove_cart,check_out

router = routers.DefaultRouter()
router.register(r'users',UserViewSet)

urlpatterns = patterns('',
    url(r'^', include(admin.site.urls)),
    url(r'^api/movies/$', MovieView.as_view(), name='movies-list'),
    url(r'^api/movies/genre/$', MovieGenreView.as_view(), name='movie-genre-list'),
    url(r'^api/movies/(?P<pk>[0-9]+)$',movieDetails),
    url(r'^api/games/$', GameView.as_view(), name='games-list'),
    url(r'^api/games/genre/$', GameGenreView.as_view(), name='game-genre-list'),
    url(r'^api/games/(?P<pk>[0-9]+)$',gameDetails),
    url(r'^api/',include(router.urls)),
    url(r'^api/login',login),
	url(r'^api/logout',logout),
	url(r'^api/authenticate',authenticate),
	url(r'^api/create_auth',create_auth),
	url(r'^api/addToCart',add_cart),
    url(r'^api/getCart',get_cart),
    url(r'^api/removeCart',remove_cart),
    url(r'^api/checkOut',check_out),
	)

urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))

admin.site.site_header = 'VADA Administrator'
