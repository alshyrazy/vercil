# Generated by Django 4.2.6 on 2023-11-01 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='image',
            field=models.ImageField(default='photos/23/10/31/Bricks.png', upload_to='photos/%y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='car',
            name='name',
            field=models.CharField(default='post', max_length=50),
        ),
    ]
