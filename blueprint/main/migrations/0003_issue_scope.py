# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-24 15:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20170923_2047'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='scope',
            field=models.CharField(default='state', max_length=64),
            preserve_default=False,
        ),
    ]
