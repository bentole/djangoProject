# Generated by Django 4.0.4 on 2022-04-19 06:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0010_alter_equipment_serial_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='serialnumber',
            name='assigned_to',
        ),
        migrations.AlterField(
            model_name='equipment',
            name='serial_number',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='demo.serialnumber'),
        ),
    ]
