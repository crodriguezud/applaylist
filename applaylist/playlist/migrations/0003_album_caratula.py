# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-09 23:54
from __future__ import unicode_literals

from django.db import migrations, models
import playlist.models


class Migration(migrations.Migration):

    dependencies = [
        ('playlist', '0002_auto_20170105_0053'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='caratula',
            field=models.ImageField(blank=True, height_field=512, null=True, upload_to=playlist.models.cargar_imagen, width_field=512),
        ),
    ]