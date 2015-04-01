# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0005_auto_20150317_1331'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='description',
            field=models.CharField(max_length=400, null=True),
            preserve_default=True,
        ),
    ]
