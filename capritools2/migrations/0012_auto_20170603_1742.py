# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-03 17:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('capritools2', '0011_auto_20170603_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='affiliation',
            name='alliance',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='localscan_affiliations', to='capritools2.Alliance'),
        ),
        migrations.AlterField(
            model_name='affiliation',
            name='corporation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='localscan_affiliations', to='capritools2.Corporation'),
        ),
    ]
