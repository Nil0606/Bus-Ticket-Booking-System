# Generated by Django 4.0.4 on 2022-05-01 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_bus_bus_name_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='ticktes',
            field=models.IntegerField(default=1),
        ),
    ]
