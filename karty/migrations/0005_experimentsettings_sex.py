# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-17 10:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('karty', '0004_auto_20170215_1532'),
    ]

    operations = [
        migrations.AddField(
            model_name='experimentsettings',
            name='sex',
            field=models.CharField(choices=[('1', 'Grupa kontrolna'), ('2', 'Grupa eksperymentalna pierwsza'), ('3', 'Grupa eksperymentalna druga')], default='F', max_length=1),
        ),
    ]