# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Load',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('commodity', models.CharField(max_length=17, verbose_name=b'Commodity', choices=[(b'Lime', b'Lime'), (b'Sand', b'Sand'), (b'Stone', b'Stone'), (b'Coal', b'Coal'), (b'Coke', b'Coke'), (b'Metal', b'Metal'), (b'Stainless', b'Stainless Steel'), (b'Feed', b'Feed Ingrediants'), (b'Glass', b'Glass'), (b'Produce', b'Produce'), (b'Other', b'Other')])),
                ('commodity_details', models.CharField(max_length=30, null=True, verbose_name=b'Commodity Details', blank=True)),
                ('shipper', models.CharField(max_length=40, verbose_name=b'Shipper')),
                ('origin_city', models.CharField(max_length=20, verbose_name=b'Origin City')),
                ('origin_state', models.CharField(max_length=2, verbose_name=b'Origin State')),
                ('shipperNumber', models.CharField(max_length=12, null=True, verbose_name=b'Shipper Phone Number', blank=True)),
                ('shipperPickupHours', models.CharField(max_length=20, null=True, verbose_name=b'Available Pick up Times', blank=True)),
                ('reciever', models.CharField(max_length=40, verbose_name=b'Reciever')),
                ('reciever_city', models.CharField(max_length=20, verbose_name=b'Destination City')),
                ('reciever_state', models.CharField(max_length=2, verbose_name=b'Destination State')),
                ('recieverNumber', models.CharField(max_length=12, null=True, verbose_name=b'Reciever Phone Number', blank=True)),
                ('recieverDropOffHours', models.CharField(max_length=20, null=True, verbose_name=b'Available Drop off Times', blank=True)),
                ('special_instructions', models.CharField(max_length=40, null=True, verbose_name=b'Special Instructions/Reference Numbers', blank=True)),
                ('customer', models.CharField(default=b'', max_length=40, verbose_name=b'Customer')),
                ('carrier', models.CharField(default=b'', max_length=40, verbose_name=b'Carrier')),
                ('date', models.DateField(help_text=b'Date load will appear in application')),
                ('pickupDate', models.DateField()),
                ('recieveDate', models.DateField()),
                ('brokerRate', models.DecimalField(max_digits=7, decimal_places=2)),
                ('brokerPercent', models.DecimalField(default=0.0, max_digits=2, decimal_places=2)),
                ('bfsc', models.DecimalField(default=0.0, max_digits=2, decimal_places=2)),
                ('carrierRate', models.DecimalField(max_digits=7, decimal_places=2)),
                ('carrierPercent', models.DecimalField(default=0.0, max_digits=2, decimal_places=2)),
                ('cfsc', models.DecimalField(default=0.0, max_digits=2, decimal_places=2)),
                ('loadConfirmed', models.BooleanField(default=False, verbose_name=b'Confirmed')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
