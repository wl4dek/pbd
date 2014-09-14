# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('user_ptr', models.OneToOneField(primary_key=True, parent_link=True, serialize=False, auto_created=True, to=settings.AUTH_USER_MODEL)),
                ('salario', models.DecimalField(verbose_name='Salário', blank=True, max_digits=6, decimal_places=2)),
                ('funcao', models.CharField(verbose_name='Funçao', max_length=45, blank=True)),
            ],
            options={
                'verbose_name_plural': 'Funcionários',
                'verbose_name': 'Funcionário',
                'ordering': ['username'],
            },
            bases=('accounts.user',),
        ),
    ]
