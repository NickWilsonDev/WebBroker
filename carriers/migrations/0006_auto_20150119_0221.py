# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carriers', '0005_auto_20150119_0002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrier',
            name='contact_name',
            field=models.CharField(max_length=20, verbose_name=b'Contact name', blank=True),
            preserve_default=True,
        ),
    ]
