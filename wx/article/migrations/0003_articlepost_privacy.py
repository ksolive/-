# Generated by Django 2.1.7 on 2020-04-22 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20190403_2129'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlepost',
            name='privacy',
            field=models.IntegerField(default=0),
        ),
    ]
