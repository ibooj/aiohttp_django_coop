# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-09 14:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_auto_20160309_1310'),
    ]

    operations = [
        migrations.AddField(
            model_name='channel',
            name='slug',
            field=models.SlugField(default='slug', verbose_name='Slug'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='channel',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Title'),
        ),
    ]