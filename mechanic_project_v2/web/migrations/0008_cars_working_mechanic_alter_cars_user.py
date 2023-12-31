# Generated by Django 4.2.4 on 2023-08-09 19:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_remove_serviceuser_cars_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='cars',
            name='working_mechanic',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='cars_serviced', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='cars',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='cars_owned', to=settings.AUTH_USER_MODEL),
        ),
    ]
