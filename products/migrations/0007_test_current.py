# Generated by Django 4.2.6 on 2023-11-01 14:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_test_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='current',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
