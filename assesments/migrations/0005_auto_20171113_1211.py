# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-13 20:11
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('assesments', '0004_auto_20171113_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assesment',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 13, 20, 11, 24, 883456, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='assesment',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 13, 20, 11, 24, 883456, tzinfo=utc)),
        ),
    ]
