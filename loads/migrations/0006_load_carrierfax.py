# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loads', '0005_auto_20150410_1451'),
    ]

    operations = [
        migrations.AddField(
            model_name='load',
            name='carrierFax',
            field=models.CharField(max_length=11, null=True, verbose_name=b'Carrier Fax', blank=True),
            preserve_default=True,
        ),
    ]
