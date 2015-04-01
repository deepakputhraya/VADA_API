# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_auto_20150401_0202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoppingcart',
            name='games',
            field=models.ManyToManyField(default=None, to='game.Game', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='shoppingcart',
            name='movies',
            field=models.ManyToManyField(default=None, to='movie.Movie', null=True, blank=True),
            preserve_default=True,
        ),
    ]
