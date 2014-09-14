# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('nome', models.CharField(verbose_name='Nome', max_length=45)),
                ('quantidade', models.IntegerField(verbose_name='Quantidade')),
                ('valor_venda', models.DecimalField(verbose_name='Valor Venda', blank=True, max_digits=5, decimal_places=2)),
                ('valor_locacao', models.DecimalField(verbose_name='Valor Locação', blank=True, max_digits=5, decimal_places=2)),
                ('date_joined', models.DateTimeField(verbose_name='Data de Entrada', auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Produtos',
                'verbose_name': 'Produto',
                'ordering': ['nome'],
            },
            bases=(models.Model,),
        ),
    ]
