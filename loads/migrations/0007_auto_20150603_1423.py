# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loads', '0006_load_carrierfax'),
    ]

    operations = [
        migrations.AddField(
            model_name='load',
            name='carrierEmail',
            field=models.CharField(max_length=40, null=True, verbose_name=b'Carrier Email', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='load',
            name='special_instructions',
            field=models.CharField(max_length=100, null=True, verbose_name=b'Special Instructions/Reference Numbers', blank=True),
            preserve_default=True,
        ),
    ]
