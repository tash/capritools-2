# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-12 22:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('capritools2', '0037_auto_20170612_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fleet_member',
            name='squad',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='members', to='capritools2.Fleet_Squad'),
        ),
        migrations.AlterField(
            model_name='fleet_member',
            name='wing',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='members', to='capritools2.Fleet_Wing'),
        ),
    ]
