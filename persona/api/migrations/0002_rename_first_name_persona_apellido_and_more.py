# Generated by Django 4.2.2 on 2024-03-14 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='persona',
            old_name='first_name',
            new_name='apellido',
        ),
        migrations.RenameField(
            model_name='persona',
            old_name='last_name',
            new_name='nombre',
        ),
    ]