# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-20 11:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0004_auto_20171019_0958'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='processed',
            field=models.CharField(max_length=3, null=True),
        ),
    ]
