# Generated by Django 2.2.24 on 2022-05-13 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0018_auto_20220513_0029'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flat',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='owner_pure_phone',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='owners_phonenumber',
        ),
    ]
