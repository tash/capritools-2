# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-15 16:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capritools2', '0047_auto_20170614_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fleet',
            name='key',
            field=models.CharField(db_index=True, max_length=7),
        ),
    ]