# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import core.models
import geoposition.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.TextField()),
                ('position', geoposition.fields.GeopositionField(max_length=42)),
                ('description', models.TextField(null=True, blank=True)),
                ('category', models.CharField(max_length=3, choices=[(b'R', b'Restaurant'), (b'B', b'Bar'), (b'F', b'Fast Food'), (b'V', b'Venue')])),
                ('image_file', models.ImageField(null=True, upload_to=core.models.get_file_path, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
