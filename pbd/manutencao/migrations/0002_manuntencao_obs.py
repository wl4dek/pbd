# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('manutencao', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='manuntencao',
            name='obs',
            field=models.TextField(default=datetime.date(2014, 9, 12), verbose_name='Obs'),
            preserve_default=False,
        ),
    ]
