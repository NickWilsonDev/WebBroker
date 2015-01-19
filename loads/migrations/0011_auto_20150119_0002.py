# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loads', '0010_auto_20150118_2354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='load',
            name='recieverNumber',
            field=models.CharField(max_length=12, null=True, verbose_name=b'Reciever Phone Number', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='load',
            name='shipperNumber',
            field=models.CharField(max_length=12, null=True, verbose_name=b'Shipper Phone Number', blank=True),
            preserve_default=True,
        ),
    ]
