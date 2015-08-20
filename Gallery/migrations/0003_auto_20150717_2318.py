# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Gallery', '0002_auto_20150717_2236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='description',
            field=models.CharField(max_length=80, null=True, verbose_name=b'Description of Photo', blank=True),
            preserve_default=True,
        ),
    ]
