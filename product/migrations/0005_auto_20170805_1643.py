# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-08-05 12:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20170805_1632'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='category',
            new_name='productcategory',
        ),
    ]
