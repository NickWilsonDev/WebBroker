# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('carriers', '0002_auto_20150226_1508'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrier',
            name='auto_ins_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='carrier',
            name='cargo_ins_amount',
            field=models.DecimalField(default=0, max_digits=9, decimal_places=2),
        ),
        migrations.AddField(
            model_name='carrier',
            name='cargo_ins_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='carrier',
            name='general_ins_date',
            field=models.DateField(default=datetime.date.today, help_text=b'Date Insurance expires'),
        ),
        migrations.AddField(
            model_name='carrier',
            name='workerscomp_ins_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='carrier',
            name='workerscomp_waiver',
            field=models.BooleanField(default=False, verbose_name=b'Waiver'),
        ),
    ]
