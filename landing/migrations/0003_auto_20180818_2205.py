# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-18 19:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0002_auto_20180817_1758'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subscriber',
            options={'verbose_name': 'My Subscriber', 'verbose_name_plural': 'A lot of Subscribers'},
        ),
        migrations.RemoveField(
            model_name='subscriber',
            name='phone_num',
        ),
    ]
