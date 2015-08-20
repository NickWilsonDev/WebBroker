# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Gallery', '0003_auto_20150717_2318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='image',
            field=models.ImageField(null=True, upload_to=b'/media/', blank=True),
            preserve_default=True,
        ),
    ]
