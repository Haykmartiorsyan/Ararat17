# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-01 07:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0005_auto_20170804_1752'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ContactForm',
        ),
    ]
