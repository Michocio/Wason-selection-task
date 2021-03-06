# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-24 15:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('karty', '0013_gil_data_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='experimentsettings',
            name='number_of_training_sets',
            field=models.IntegerField(default=25, verbose_name='Liczba zadań fazy traningowej GIL wraz z wyborem kart - pomiar'),
        ),
        migrations.AddField(
            model_name='task',
            name='used',
            field=models.BooleanField(default=0),
        ),
    ]
