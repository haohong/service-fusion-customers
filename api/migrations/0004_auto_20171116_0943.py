# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-16 09:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20171116_0854'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Person',
        ),
        migrations.RenameField(
            model_name='address',
            old_name='user',
            new_name='owner',
        ),
        migrations.RenameField(
            model_name='email',
            old_name='user',
            new_name='owner',
        ),
        migrations.RenameField(
            model_name='phonenumber',
            old_name='user',
            new_name='owner',
        ),
    ]
