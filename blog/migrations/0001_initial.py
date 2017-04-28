# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('nome', models.CharField(verbose_name='Nome', max_length=100)),
                ('ordem', models.IntegerField(verbose_name='Ordem')),
                ('ativo', models.IntegerField(verbose_name='Ativo', default=0)),
                ('convidado', models.CharField(verbose_name='Convidado', max_length=100, blank=True)),
            ],
            options={
                'verbose_name_plural': 'Itens',
                'verbose_name': 'Item',
                'ordering': ['ordem'],
            },
        ),
    ]
