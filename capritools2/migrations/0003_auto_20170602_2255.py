# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-02 22:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capritools2', '0002_auto_20170602_2234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dscan',
            name='key',
            field=models.CharField(db_index=True, max_length=40, unique=True),
        ),
    ]
