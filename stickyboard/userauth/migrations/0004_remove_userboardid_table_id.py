# Generated by Django 2.0.5 on 2018-06-11 07:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0003_auto_20180606_1504'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userboardid',
            name='table_id',
        ),
    ]