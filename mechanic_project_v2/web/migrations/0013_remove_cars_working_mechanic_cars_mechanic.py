# Generated by Django 4.2.4 on 2023-08-09 20:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0012_alter_cars_working_mechanic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cars',
            name='working_mechanic',
        ),
        migrations.AddField(
            model_name='cars',
            name='mechanic',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cars_worked_on', to=settings.AUTH_USER_MODEL),
        ),
    ]