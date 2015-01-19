# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carriers', '0002_auto_20150118_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrier',
            name='email',
            field=models.CharField(default=b'', max_length=20, verbose_name=b'Email address'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='carrier',
            name='mc_id',
            field=models.CharField(default=b'', max_length=8, verbose_name=b'Motor carrier number'),
            preserve_default=True,
        ),
    ]
