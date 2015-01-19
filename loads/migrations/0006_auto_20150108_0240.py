# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loads', '0005_auto_20150107_0447'),
    ]

    operations = [
        migrations.AddField(
            model_name='load',
            name='bfsc',
            field=models.DecimalField(null=True, max_digits=2, decimal_places=2, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='load',
            name='cfsc',
            field=models.DecimalField(null=True, max_digits=2, decimal_places=2, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='load',
            name='date',
            field=models.DateField(help_text=b'Date load will appear in application'),
            preserve_default=True,
        ),
    ]
