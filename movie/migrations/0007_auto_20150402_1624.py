# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0006_movie_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='deposit',
            field=models.IntegerField(default=100),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='movie',
            name='rent',
            field=models.IntegerField(default=50),
            preserve_default=True,
        ),
    ]
