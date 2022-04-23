# Generated by Django 2.2.24 on 2022-04-23 12:35

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0012_auto_20220423_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='owner_pure_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, default='NATIONAL', max_length=128, region=None, verbose_name='Нормализованный номер телефона'),
        ),
    ]
