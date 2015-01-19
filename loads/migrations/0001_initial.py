# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Load',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('commodity', models.CharField(max_length=17, verbose_name=b'Commodity', choices=[(b'Lime', b'Lime'), (b'Sand', b'Sand'), (b'Stone', b'Stone'), (b'Coal', b'Coal'), (b'Coke', b'Coke'), (b'Metal', b'Metal'), (b'Stainless', b'Stainless Steel'), (b'Feed', b'Feed Ingrediants'), (b'Glass', b'Glass'), (b'Produce', b'Produce'), (b'Other', b'Other')])),
                ('commodity_details', models.CharField(max_length=30, null=True, verbose_name=b'Commodity Details')),
                ('shipper', models.CharField(max_length=40, verbose_name=b'Shipper')),
                ('origin_city', models.CharField(max_length=20, verbose_name=b'Origin City')),
                ('origin_state', models.CharField(max_length=2, verbose_name=b'Origin State')),
                ('reciever', models.CharField(max_length=40, verbose_name=b'Reciever')),
                ('reciever_city', models.CharField(max_length=20, verbose_name=b'Destination City')),
                ('reciever_state', models.CharField(max_length=2, verbose_name=b'Destination State')),
                ('special_instructions', models.CharField(max_length=40, null=True, verbose_name=b'Special Instructions/Reference Numbers')),
                ('customer', models.CharField(default=b'', max_length=40, verbose_name=b'Customer')),
                ('carrier', models.CharField(default=b'', max_length=40, verbose_name=b'Carrier')),
                ('date', models.DateField(default=datetime.date(2014, 12, 25), auto_now_add=True)),
                ('load_confirmed', models.BooleanField(default=False, verbose_name=b'Confirmed')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
