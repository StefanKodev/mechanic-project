# Generated by Django 4.2.4 on 2023-08-09 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_serviceuser_cars_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='serviceuser',
            name='cars_count',
        ),
    ]
