# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loads', '0008_auto_20150108_0608'),
    ]

    operations = [
        migrations.AddField(
            model_name='load',
            name='recieverDropOffHours',
            field=models.CharField(max_length=20, null=True, verbose_name=b'Available Drop off Times', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='load',
            name='recieverNumber',
            field=models.CharField(max_length=10, null=True, verbose_name=b'Reciever Phone Number', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='load',
            name='shipperNumber',
            field=models.CharField(max_length=10, null=True, verbose_name=b'Shipper Phone Number', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='load',
            name='shipperPickupHours',
            field=models.CharField(max_length=20, null=True, verbose_name=b'Available Pick up Times', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='load',
            name='carrier',
            field=models.CharField(default=b'', max_length=40, verbose_name=b'Carrier', choices=[['democarrier', 'democarrier'], ['Emmett Wilson Trucking Inc', 'Emmett Wilson Trucking Inc']]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='load',
            name='customer',
            field=models.CharField(default=b'', max_length=40, verbose_name=b'Customer', choices=[['democustomer', 'democustomer'], ['North Carolina Farm Bureau Marketing', 'North Carolina Farm Bureau Marketing']]),
            preserve_default=True,
        ),
    ]
