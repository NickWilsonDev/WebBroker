# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carriers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrier',
            name='fax_number',
            field=models.CharField(max_length=10, verbose_name=b'Fax number'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='carrier',
            name='mc_id',
            field=models.CharField(default=b'', max_length=7, verbose_name=b'Motor carrier number'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='carrier',
            name='phone_number',
            field=models.CharField(max_length=10, verbose_name=b'Phone number'),
            preserve_default=True,
        ),
    ]
