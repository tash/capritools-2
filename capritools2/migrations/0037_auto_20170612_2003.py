# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-12 20:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('capritools2', '0036_auto_20170612_1801'),
    ]

    operations = [
        migrations.AddField(
            model_name='fleet_member',
            name='boss',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='fleet_member',
            name='corporation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fleet_members', to='capritools2.Corporation'),
        ),
        migrations.AlterField(
            model_name='fleet_member',
            name='join_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
