# Generated by Django 2.0.5 on 2018-06-06 15:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('userauth', '0002_userboardid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='userboardid',
            name='user',
        ),
        migrations.AddField(
            model_name='userboardid',
            name='user',
            field=models.ManyToManyField(related_name='userboardid', to=settings.AUTH_USER_MODEL),
        ),
    ]
