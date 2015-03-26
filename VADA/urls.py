from django.conf.urls import patterns, include, url
from django.contrib import admin
from movie.views import MovieView,MovieGenreView
from django.conf import settings


urlpatterns = patterns('',
    url(r'^', include(admin.site.urls)),
    url(r'^api/movies/$', MovieView.as_view(), name='movies-list'),
    url(r'^api/movies/genre/$', MovieGenreView.as_view(), name='movie-genre-list'),
    )

urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))
