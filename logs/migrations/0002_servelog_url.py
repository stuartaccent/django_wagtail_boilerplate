# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-11 22:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='servelog',
            name='url',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
