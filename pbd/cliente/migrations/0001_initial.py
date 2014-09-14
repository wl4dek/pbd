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
            name='Cliente',
            fields=[
                ('user_ptr', models.OneToOneField(primary_key=True, parent_link=True, serialize=False, auto_created=True, to=settings.AUTH_USER_MODEL)),
                ('locatario', models.CharField(verbose_name='Locatário', max_length=45)),
                ('cnpj', models.CharField(verbose_name='CNPJ', max_length=18)),
                ('rg', models.CharField(verbose_name='RG', max_length=45)),
                ('municipio', models.CharField(verbose_name='Insc. Municípal', max_length=45)),
                ('contato', models.CharField(verbose_name='Contato', max_length=45)),
            ],
            options={
                'verbose_name_plural': 'Clientes',
                'verbose_name': 'Cliente',
                'ordering': ['username'],
            },
            bases=('accounts.user',),
        ),
    ]
