# Generated by Django 2.2.6 on 2020-04-23 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0005_auto_20200423_1936'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='experts',
            options={'verbose_name': '专家', 'verbose_name_plural': '专家'},
        ),
        migrations.AlterModelOptions(
            name='myuser',
            options={'verbose_name': '普通用户', 'verbose_name_plural': '普通用户'},
        ),
        migrations.AlterModelOptions(
            name='volunteers',
            options={'verbose_name': '志愿者', 'verbose_name_plural': '志愿者'},
        ),
    ]
