# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-15 09:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20170715_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='con_signup',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]