# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loads', '0011_auto_20150119_0002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='load',
            name='customer',
            field=models.CharField(default=b'', max_length=40, verbose_name=b'Customer', choices=[['democustomer', 'democustomer'], ['North Carolina Farm Bureau Marketing', 'North Carolina Farm Bureau Marketing'], ['democustomer7', 'democustomer7'], ['democustomer2', 'democustomer2']]),
            preserve_default=True,
        ),
    ]
