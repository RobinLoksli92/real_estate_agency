# Generated by Django 2.2.24 on 2022-04-23 17:48

from django.db import migrations


def copy_owners_from_flat_to_owner(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    for flat in Flat.objects.all():
        Owner.objects.get_or_create(
            owner_name=flat.owner,
            owners_phonenumber=flat.owners_phonenumber,
            owner_pure_phone=flat.owner_pure_phone
            )


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0015_auto_20220423_1942'),
    ]

    operations = [
        migrations.RunPython(copy_owners_from_flat_to_owner)
    ]