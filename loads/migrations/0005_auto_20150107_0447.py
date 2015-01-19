# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loads', '0004_auto_20150107_0400'),
    ]

    operations = [
        migrations.AddField(
            model_name='load',
            name='brokerPercent',
            field=models.DecimalField(null=True, max_digits=2, decimal_places=2, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='load',
            name='carrierPercent',
            field=models.DecimalField(null=True, max_digits=2, decimal_places=2, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='load',
            name='commodity_details',
            field=models.CharField(max_length=30, null=True, verbose_name=b'Commodity Details', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='load',
            name='date',
            field=models.DateField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='load',
            name='special_instructions',
            field=models.CharField(max_length=40, null=True, verbose_name=b'Special Instructions/Reference Numbers', blank=True),
            preserve_default=True,
        ),
    ]
