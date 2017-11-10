# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-10 03:17
from __future__ import unicode_literals

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='image_url',
            field=models.FileField(null=True, upload_to=products.models.custom_filename),
        ),
    ]
