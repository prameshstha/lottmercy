# Generated by Django 3.1 on 2020-09-07 01:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homePage', '0002_auto_20200907_1030'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetails',
            name='user_name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='gamenumber',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 7, 10, 33, 48, 814852)),
        ),
    ]
