# Generated by Django 2.0.dev20170906232138 on 2017-09-20 09:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='account',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='login.Account'),
        ),
    ]