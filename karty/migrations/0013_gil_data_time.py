# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-21 17:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('karty', '0012_remove_currentsettings_mode'),
    ]

    operations = [
        migrations.AddField(
            model_name='gil_data',
            name='time',
            field=models.FloatField(default=0.0),
        ),
    ]
