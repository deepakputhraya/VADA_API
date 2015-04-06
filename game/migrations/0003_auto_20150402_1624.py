# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_game_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='deposit',
            field=models.IntegerField(default=100),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='game',
            name='rent',
            field=models.IntegerField(default=50),
            preserve_default=True,
        ),
    ]
