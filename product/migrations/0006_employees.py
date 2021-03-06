# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-08-05 15:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20170805_1643'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=64, null=True)),
                ('description', models.TextField(blank=True, default=None, null=True)),
                ('index', models.IntegerField(default=1)),
                ('image', models.ImageField(upload_to='employees_image')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Employees',
                'verbose_name': 'Employee',
            },
        ),
    ]
