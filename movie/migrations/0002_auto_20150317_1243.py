# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='poster',
            field=models.ImageField(upload_to=b'movie-posters/'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='moviegenre',
            name='name',
            field=models.CharField(unique=True, max_length=30),
            preserve_default=True,
        ),
    ]
