# Generated by Django 2.2.24 on 2022-04-20 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_flat_new_bulding'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='new_bulding',
            field=models.NullBooleanField(db_index=True, verbose_name='Новостройка'),
        ),
    ]