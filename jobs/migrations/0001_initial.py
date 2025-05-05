# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('job_name', models.CharField(unique=True, max_length=30, verbose_name=b'Job Name')),
                ('commodity', models.CharField(max_length=17, verbose_name=b'Commodity', choices=[(b'Lime', b'Lime'), (b'Sand', b'Sand'), (b'Stone', b'Stone'), (b'Coal', b'Coal'), (b'Coke', b'Coke'), (b'Metal', b'Metal'), (b'Stainless', b'Stainless Steel'), (b'Feed', b'Feed Ingrediants'), (b'Glass', b'Glass'), (b'Produce', b'Produce'), (b'Other', b'Other')])),
                ('commodity_details', models.CharField(max_length=30, null=True, verbose_name=b'Commodity Details', blank=True)),
                ('shipper', models.CharField(max_length=40, verbose_name=b'Shipper')),
                ('shipper_street_address', models.CharField(max_length=40, null=True, verbose_name=b'Street Address', blank=True)),
                ('origin_city', models.CharField(max_length=20, verbose_name=b'Origin City')),
                ('origin_state', models.CharField(max_length=2, verbose_name=b'Origin State')),
                ('shipperNumber', models.CharField(max_length=12, null=True, verbose_name=b'Shipper Phone Number', blank=True)),
                ('shipperPickupHours', models.CharField(max_length=20, null=True, verbose_name=b'Available Pick up Times', blank=True)),
                ('reciever', models.CharField(max_length=40, verbose_name=b'Reciever')),
                ('reciever_street_address', models.CharField(max_length=40, null=True, verbose_name=b'Street Address', blank=True)),
                ('reciever_city', models.CharField(max_length=20, verbose_name=b'Destination City')),
                ('reciever_state', models.CharField(max_length=2, verbose_name=b'Destination State')),
                ('recieverNumber', models.CharField(max_length=12, null=True, verbose_name=b'Reciever Phone Number', blank=True)),
                ('recieverDropOffHours', models.CharField(max_length=20, null=True, verbose_name=b'Available Drop off Times', blank=True)),
                ('special_instructions', models.CharField(max_length=40, null=True, verbose_name=b'Special Instructions/Reference Numbers', blank=True)),
                ('brokerRate', models.DecimalField(max_digits=7, decimal_places=2)),
                ('bfsc', models.DecimalField(default=0.0, max_digits=2, decimal_places=2)),
                ('carrierRate', models.DecimalField(max_digits=7, decimal_places=2)),
                ('cfsc', models.DecimalField(default=0.0, max_digits=2, decimal_places=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
