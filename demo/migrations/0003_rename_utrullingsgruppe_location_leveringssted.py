# Generated by Django 4.0.4 on 2022-04-18 19:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0002_serialnumber_alter_location_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='utrullingsgruppe',
            new_name='leveringssted',
        ),
    ]
