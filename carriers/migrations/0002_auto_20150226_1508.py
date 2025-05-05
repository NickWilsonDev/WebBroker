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
            name='email',
            field=models.CharField(default=b'', max_length=40, verbose_name=b'Email address', blank=True),
            preserve_default=True,
        ),
    ]
