# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_auto_20150118_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='email_address',
            field=models.CharField(default=b'', max_length=30, null=True, verbose_name=b'Email Address'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='customer',
            name='fax_number',
            field=models.CharField(default=b'', max_length=10, null=True, verbose_name=b'Fax number'),
            preserve_default=True,
        ),
    ]
