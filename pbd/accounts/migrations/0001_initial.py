# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(verbose_name='last login', default=django.utils.timezone.now)),
                ('is_superuser', models.BooleanField(verbose_name='superuser status', help_text='Designates that this user has all permissions without explicitly assigning them.', default=False)),
                ('username', models.CharField(unique=True, verbose_name='Nome', max_length=45)),
                ('email', models.EmailField(unique=True, verbose_name='E-mail', max_length=75)),
                ('endereco', models.CharField(verbose_name='Endereço', max_length=200, blank=True)),
                ('bairro', models.CharField(verbose_name='Bairro', max_length=200, blank=True)),
                ('cidade', models.CharField(verbose_name='Cidade', max_length=100, blank=True)),
                ('estado', models.CharField(verbose_name='Estado', max_length=100, blank=True)),
                ('cep', models.CharField(verbose_name='CEP', max_length=10, blank=True)),
                ('cpf', models.CharField(unique=True, verbose_name='CPF', max_length=14, blank=True)),
                ('is_active', models.BooleanField(verbose_name='Está ativo?', default=True)),
                ('is_staff', models.BooleanField(verbose_name='É da equipe?', default=False)),
                ('date_joined', models.DateTimeField(verbose_name='Data de Entrada', auto_now_add=True)),
                ('groups', models.ManyToManyField(related_query_name='user', to='auth.Group', verbose_name='groups', help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.', blank=True, related_name='user_set')),
            ],
            options={
                'verbose_name_plural': 'Usuários',
                'verbose_name': 'Usuário',
                'ordering': ['username'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PasswordReset',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('key', models.CharField(unique=True, verbose_name='Chave', max_length=100)),
                ('created_at', models.DateTimeField(verbose_name='Criado em', auto_now_add=True)),
                ('confirmed', models.BooleanField(verbose_name='Confirmado?', default=False)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='Usuário', related_name='resets')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Telefone',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('telefone', models.CharField(verbose_name='Telefone', max_length=18)),
            ],
            options={
                'verbose_name_plural': 'Telefones',
                'verbose_name': 'Telefone',
                'ordering': ['telefone'],
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='user',
            name='telefones',
            field=models.ManyToManyField(to='accounts.Telefone'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(related_query_name='user', to='auth.Permission', verbose_name='user permissions', help_text='Specific permissions for this user.', blank=True, related_name='user_set'),
            preserve_default=True,
        ),
    ]
