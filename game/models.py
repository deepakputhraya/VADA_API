from django.db import models

class GameGenre(models.Model):
    name = models.CharField(max_length=30)
    def __unicode__(self):
        return u'%s' % (self.name)

class Game(models.Model):
    title = models.CharField(max_length=50)
    developer = models.CharField(max_length=50)
    rating = models.IntegerField()
    genre = models.ManyToManyField(GameGenre)
    stock = models.IntegerField()
    poster = models.ImageField()
    releaseDate = models.DateField()
    description = models.CharField(max_length=400,null=True)

    def __unicode__(self):
        return u'%s' % (self.title)
