# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manuntencao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('data', models.DateTimeField(verbose_name='Data')),
                ('valor_gasto', models.DecimalField(verbose_name='Valor Gasto', blank=True, max_digits=6, decimal_places=2)),
                ('produto', models.ForeignKey(to='produto.Produto')),
            ],
            options={
                'verbose_name_plural': 'Manunteções',
                'verbose_name': 'Manunteção',
                'ordering': ['produto'],
            },
            bases=(models.Model,),
        ),
    ]
