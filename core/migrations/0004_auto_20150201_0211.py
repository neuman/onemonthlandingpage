# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_location_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='rating',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'None'), (1, b'*'), (2, b'**'), (3, b'***'), (4, b'****'), (5, b'*****')]),
            preserve_default=True,
        ),
    ]
