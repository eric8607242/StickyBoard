# Generated by Django 2.0.5 on 2018-07-03 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0008_invitestatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='invitestatus',
            name='board_name',
            field=models.CharField(default='123', max_length=20),
            preserve_default=False,
        ),
    ]
