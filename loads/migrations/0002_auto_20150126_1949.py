# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loads', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='load',
            name='reciever_street_address',
            field=models.CharField(max_length=40, null=True, verbose_name=b'Street Address', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='load',
            name='shipper_street_address',
            field=models.CharField(max_length=40, null=True, verbose_name=b'Street Address', blank=True),
            preserve_default=True,
        ),
    ]
