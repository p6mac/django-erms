# Generated by Django 2.0.dev20170906232138 on 2017-09-12 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_auto_20170912_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='account_id',
            field=models.IntegerField(),
        ),
    ]