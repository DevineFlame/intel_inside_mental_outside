# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-22 19:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_side', '0002_auto_20170322_1848'),
    ]

    operations = [
        migrations.CreateModel(
            name='sqlerror',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('error', models.CharField(max_length=1000)),
                ('sql', models.CharField(max_length=1000)),
                ('db', models.CharField(max_length=1000)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'sqlerror',
            },
        ),
    ]
