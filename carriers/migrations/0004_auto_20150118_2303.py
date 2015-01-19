# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carriers', '0003_auto_20150118_2259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrier',
            name='contact_name',
            field=models.CharField(max_length=20, verbose_name=b'Contact number', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='carrier',
            name='email',
            field=models.CharField(default=b'', max_length=20, verbose_name=b'Email address', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='carrier',
            name='fax_number',
            field=models.CharField(max_length=10, verbose_name=b'Fax number', blank=True),
            preserve_default=True,
        ),
    ]
