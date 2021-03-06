# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-27 07:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('departments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('birthdate', models.DateField()),
                ('address', models.CharField(max_length=50)),
                ('age', models.CharField(max_length=121)),
                ('salary', models.IntegerField()),
                ('department', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='departments.Departments')),
            ],
            options={
                'db_table': 'employees',
            },
        ),
    ]
