# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-28 13:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='participant',
            old_name='profile_id',
            new_name='captain',
        ),
    ]
