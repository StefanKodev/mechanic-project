# Generated by Django 4.2.4 on 2023-08-08 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='serviceuser',
            name='is_mechanic',
            field=models.BooleanField(default=False),
        ),
    ]