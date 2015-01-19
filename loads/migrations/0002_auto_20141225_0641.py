# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loads', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='load',
            old_name='load_confirmed',
            new_name='loadConfirmed',
        ),
    ]
