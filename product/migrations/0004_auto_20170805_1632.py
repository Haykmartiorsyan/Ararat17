# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-08-05 12:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20170805_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(blank=True, default=None, null=True, related_name='self', to='product.ProductCategory'),
        ),
    ]
