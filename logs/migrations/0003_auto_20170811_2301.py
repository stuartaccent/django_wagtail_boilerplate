# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-11 23:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0002_servelog_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servelog',
            name='http_user_agent',
            field=models.TextField(null=True),
        ),
    ]
