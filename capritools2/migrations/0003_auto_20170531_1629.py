# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-31 16:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capritools2', '0002_auto_20170531_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marketgroup',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
