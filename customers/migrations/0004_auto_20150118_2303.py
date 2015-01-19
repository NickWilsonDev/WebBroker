# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0003_auto_20150118_2259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='email_address',
            field=models.CharField(default=b'', max_length=30, verbose_name=b'Email Address', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='customer',
            name='fax_number',
            field=models.CharField(default=b'', max_length=10, verbose_name=b'Fax number', blank=True),
            preserve_default=True,
        ),
    ]
