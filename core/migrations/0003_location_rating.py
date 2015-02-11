# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_location_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='rating',
            field=models.IntegerField(blank=True, null=True, choices=[(b'R', b'Restaurant'), (b'B', b'Bar'), (b'F', b'Fast Food'), (b'V', b'Venue')]),
            preserve_default=True,
        ),
    ]
