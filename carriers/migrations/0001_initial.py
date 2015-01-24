# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carrier',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('company_name', models.CharField(unique=True, max_length=30, verbose_name=b'Companies name')),
                ('phone_number', models.CharField(max_length=12, verbose_name=b'Phone number')),
                ('fax_number', models.CharField(max_length=12, verbose_name=b'Fax number', blank=True)),
                ('contact_name', models.CharField(max_length=20, verbose_name=b'Contact name', blank=True)),
                ('email', models.CharField(default=b'', max_length=20, verbose_name=b'Email address', blank=True)),
                ('address', models.CharField(default=b'', max_length=40, verbose_name=b'Address')),
                ('fed_id', models.CharField(default=b'', max_length=10, verbose_name=b'Federal ID')),
                ('mc_id', models.CharField(default=b'', max_length=8, verbose_name=b'Motor carrier number')),
                ('number_trucks', models.CharField(default=b'', max_length=2, verbose_name=b'Number of trucks')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
