# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0004_auto_20150118_2303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='fax_number',
            field=models.CharField(default=b'', max_length=12, verbose_name=b'Fax number', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone_number',
            field=models.CharField(max_length=12, verbose_name=b'Phone number'),
            preserve_default=True,
        ),
    ]
