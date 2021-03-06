# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-25 19:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('karty', '0014_auto_20170224_1529'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.FloatField(default=0.0)),
                ('which', models.IntegerField(default=0)),
                ('session', models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='karty.Session')),
            ],
        ),
        migrations.AlterField(
            model_name='experimentsettings',
            name='number_of_training_sets',
            field=models.IntegerField(default=2, verbose_name='Liczba zadań fazy traningowej GIL wraz z wyborem kart - pomiar'),
        ),
        migrations.AlterField(
            model_name='task',
            name='additional_description',
            field=models.CharField(default='dalsza Historyjka', max_length=1000),
        ),
    ]
