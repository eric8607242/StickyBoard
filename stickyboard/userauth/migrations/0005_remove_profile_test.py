# Generated by Django 2.0.5 on 2018-06-11 07:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0004_remove_userboardid_table_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='test',
        ),
    ]
