# Generated by Django 3.1 on 2020-09-07 01:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homePage', '0003_auto_20200907_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamenumber',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 7, 10, 34, 19, 68542)),
        ),
    ]
