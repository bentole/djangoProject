# Generated by Django 4.0.4 on 2022-04-19 06:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0009_alter_serialnumber_assigned_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='serial_number',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='demo.serialnumber'),
        ),
    ]
