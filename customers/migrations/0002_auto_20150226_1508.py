# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='email_address',
            field=models.CharField(default=b'', max_length=40, verbose_name=b'Email Address', blank=True),
            preserve_default=True,
        ),
    ]
