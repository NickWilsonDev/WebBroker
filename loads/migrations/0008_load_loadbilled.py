# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loads', '0007_auto_20150603_1423'),
    ]

    operations = [
        migrations.AddField(
            model_name='load',
            name='loadBilled',
            field=models.BooleanField(default=False, verbose_name=b'Billed'),
            preserve_default=True,
        ),
    ]
