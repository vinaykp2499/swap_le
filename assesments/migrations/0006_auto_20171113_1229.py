# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-13 20:29
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('assesments', '0005_auto_20171113_1211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assesment',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 13, 20, 29, 40, 642960, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='assesment',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 13, 20, 29, 40, 642960, tzinfo=utc)),
        ),
    ]