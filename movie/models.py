from django.db import models

class MovieGenre(models.Model):
    name = models.CharField(max_length=30,unique=True)
    def __unicode__(self):
        return u'%s' % (self.name)

class Movie(models.Model):
    title = models.CharField(max_length=50)
    director = models.CharField(max_length=50)
    language = models.CharField(max_length=30)
    description = models.CharField(max_length=400,null=True)
    rating = models.IntegerField()
    duration = models.IntegerField()
    genre = models.ManyToManyField(MovieGenre)
    stock = models.IntegerField()
    poster = models.ImageField(upload_to='movie')
    releaseDate = models.DateField()

    def __unicode__(self):
        return u'%s' % (self.title)
