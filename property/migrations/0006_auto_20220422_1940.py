# Generated by Django 2.2.24 on 2022-04-22 17:40

from django.db import migrations


def new_building_check(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    flats = Flat.objects.all()
    for flat in flats.iterator():
        flat.new_building = flat.construction_year >= 2015
        flat.save()

            
class Migration(migrations.Migration):

    dependencies = [
        ('property', '0005_auto_20220420_1244'),
    ]

    operations = [
        migrations.RunPython(new_building_check)
    ]




