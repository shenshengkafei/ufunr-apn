# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-18 05:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('console', '0004_auto_20160118_0528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='data_left',
            field=models.FloatField(default=10240),
        ),
    ]
