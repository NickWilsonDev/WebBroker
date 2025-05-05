# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loads', '0003_load_job'),
    ]

    operations = [
        migrations.AlterField(
            model_name='load',
            name='bfsc',
            field=models.DecimalField(default=0.0, max_digits=4, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='load',
            name='brokerPercent',
            field=models.DecimalField(default=0.0, max_digits=4, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='load',
            name='carrierPercent',
            field=models.DecimalField(default=0.0, max_digits=4, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='load',
            name='cfsc',
            field=models.DecimalField(default=0.0, max_digits=4, decimal_places=2),
            preserve_default=True,
        ),
    ]
