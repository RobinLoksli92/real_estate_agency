# Generated by Django 2.2.24 on 2022-04-20 10:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0004_auto_20220420_1234'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flat',
            old_name='new_bulding',
            new_name='new_building',
        ),
    ]
