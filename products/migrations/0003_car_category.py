# Generated by Django 4.2.6 on 2023-11-01 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_car_image_alter_car_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='category',
            field=models.CharField(blank=True, choices=[('phones', 'phones')], max_length=50, null=True),
        ),
    ]
