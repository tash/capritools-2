# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-03 19:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('capritools2', '0012_auto_20170603_1742'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='affiliation',
            unique_together=set([('scan', 'corporation', 'alliance')]),
        ),
    ]
