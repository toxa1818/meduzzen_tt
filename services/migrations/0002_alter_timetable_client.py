# Generated by Django 4.1.3 on 2022-12-06 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetable',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.client'),
        ),
    ]
