# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-18 02:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_id', models.CharField(max_length=20)),
                ('valid_days', models.IntegerField(default=375)),
                ('data', models.IntegerField(default=10240)),
                ('is_deleted', models.CharField(max_length=10)),
            ],
        ),
    ]
