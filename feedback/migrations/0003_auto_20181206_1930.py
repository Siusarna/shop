# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-06 17:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0002_auto_20181206_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='how_much',
            field=models.CharField(default='1', max_length=3, verbose_name='Кількість людей'),
        ),
    ]
