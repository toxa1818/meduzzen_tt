# Generated by Django 4.1.3 on 2022-12-08 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_alter_timetable_client'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Timetable',
            new_name='Entries',
        ),
    ]
