# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loads', '0002_auto_20150126_1949'),
    ]

    operations = [
        migrations.AddField(
            model_name='load',
            name='job',
            field=models.CharField(default=b'', max_length=40, null=True, verbose_name=b'Job', blank=True),
            preserve_default=True,
        ),
    ]
