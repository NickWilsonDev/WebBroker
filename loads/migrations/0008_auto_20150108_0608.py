# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loads', '0007_auto_20150108_0607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='load',
            name='bfsc',
            field=models.DecimalField(default=0, max_digits=2, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='load',
            name='brokerPercent',
            field=models.DecimalField(default=0, max_digits=2, decimal_places=2),
            preserve_default=True,
        ),
    ]
