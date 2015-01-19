# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loads', '0009_auto_20150118_2321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='load',
            name='carrier',
            field=models.CharField(default=b'', max_length=40, verbose_name=b'Carrier', choices=[['democarrier', 'democarrier'], ['Emmett Wilson Trucking Inc', 'Emmett Wilson Trucking Inc'], ['Panola Express', 'Panola Express']]),
            preserve_default=True,
        ),
    ]
