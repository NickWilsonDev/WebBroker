# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('company_name', models.CharField(unique=True, max_length=40, verbose_name=b'Company name')),
                ('contact_name', models.CharField(max_length=30, verbose_name=b'Contact name')),
                ('phone_number', models.CharField(max_length=8, verbose_name=b'Phone number')),
                ('fax_number', models.CharField(max_length=8, verbose_name=b'Fax number')),
                ('address', models.CharField(default=b'', max_length=40, verbose_name=b'Address')),
                ('email_address', models.CharField(max_length=30, null=True, verbose_name=b'Email Address')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
