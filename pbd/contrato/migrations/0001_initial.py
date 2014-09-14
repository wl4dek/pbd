# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
        ('produto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contrato',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('entrega', models.DateTimeField(verbose_name='Data de Entrega', auto_now_add=True)),
                ('hora', models.TimeField(verbose_name='Hora')),
                ('duracao', models.DateTimeField(verbose_name='Duração')),
                ('referencia', models.CharField(verbose_name='Referência Obra', max_length=200, blank=True)),
                ('endereco', models.CharField(verbose_name='Endereço Obra', max_length=200, blank=True)),
                ('bairro', models.CharField(verbose_name='Bairro da Obra', max_length=200, blank=True)),
                ('cidade', models.CharField(verbose_name='Cidade da Obra', max_length=100, blank=True)),
                ('estado', models.CharField(verbose_name='Estado da Obra', max_length=100, blank=True)),
                ('cep', models.CharField(verbose_name='CEP da Obra', max_length=10, blank=True)),
                ('desconto', models.DecimalField(verbose_name='Valor Locação', blank=True, max_digits=5, decimal_places=2)),
                ('valor_contrato', models.DecimalField(verbose_name='Valor Contrato', blank=True, max_digits=5, decimal_places=2)),
                ('cliente', models.ForeignKey(to='cliente.Cliente', blank=True, related_name='Cliente')),
                ('produto', models.ManyToManyField(to='produto.Produto', blank=True, related_name='Produtos')),
            ],
            options={
                'verbose_name_plural': 'Contratos',
                'verbose_name': 'Contrato',
                'ordering': ['cliente'],
            },
            bases=(models.Model,),
        ),
    ]
