# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-17 14:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=128)),
                ('phone_num', models.CharField(max_length=128)),
            ],
        ),
        migrations.DeleteModel(
            name='Subscribers',
        ),
    ]
