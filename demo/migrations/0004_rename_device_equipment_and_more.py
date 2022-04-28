# Generated by Django 4.0.4 on 2022-04-18 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0003_rename_utrullingsgruppe_location_leveringssted'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Device',
            new_name='Equipment',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='annen_info',
            new_name='other_info',
        ),
        migrations.RemoveField(
            model_name='location',
            name='leveringssted',
        ),
        migrations.AddField(
            model_name='location',
            name='circuit_info',
            field=models.CharField(max_length=3, null=True, verbose_name='Samband'),
        ),
        migrations.AddField(
            model_name='location',
            name='delivery_place',
            field=models.CharField(choices=[('Alta', 'Alta'), ('Kristiansund', 'Kristiansund')], max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='emp',
            field=models.CharField(choices=[('OK', 'OK')], max_length=2, null=True, verbose_name='EMP'),
        ),
        migrations.AddField(
            model_name='location',
            name='extra_switches',
            field=models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], max_length=3, null=True, verbose_name='Lokasjon med ekstra svitsjer'),
        ),
        migrations.AddField(
            model_name='location',
            name='network',
            field=models.CharField(choices=[('P1, P2, O, Kjernerutere', 'P1, P2, O, Kjernerutere'), ('P1, P2, O', 'P1, P2, O')], max_length=255, null=True, verbose_name='Nettverk'),
        ),
        migrations.AddField(
            model_name='location',
            name='technical_location',
            field=models.CharField(max_length=255, null=True, verbose_name='Teknisk lokasjonsnavn'),
        ),
        migrations.AlterField(
            model_name='location',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Navn'),
        ),
    ]