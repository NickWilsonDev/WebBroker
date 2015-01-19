# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('loads', '0003_auto_20150106_2339'),
    ]

    operations = [
        migrations.AddField(
            model_name='load',
            name='pickupDate',
            field=models.DateField(default=datetime.datetime(2015, 1, 7, 4, 0, 44, 497394, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='load',
            name='recieveDate',
            field=models.DateField(default=datetime.datetime(2015, 1, 7, 4, 0, 54, 309987, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='load',
            name='date',
            field=models.DateField(default=datetime.date(2015, 1, 7), auto_now_add=True),
            preserve_default=True,
        ),
    ]
