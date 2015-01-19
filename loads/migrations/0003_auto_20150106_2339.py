# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('loads', '0002_auto_20141225_0641'),
    ]

    operations = [
        migrations.AddField(
            model_name='load',
            name='brokerRate',
            field=models.DecimalField(default=0, max_digits=7, decimal_places=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='load',
            name='carrierRate',
            field=models.DecimalField(default=0, max_digits=7, decimal_places=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='load',
            name='carrier',
            field=models.CharField(default=b'', max_length=40, verbose_name=b'Carrier', choices=[['democarrier', 'democarrier']]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='load',
            name='customer',
            field=models.CharField(default=b'', max_length=40, verbose_name=b'Customer', choices=[['democustomer', 'democustomer']]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='load',
            name='date',
            field=models.DateField(default=datetime.date(2015, 1, 6), auto_now_add=True),
            preserve_default=True,
        ),
    ]
