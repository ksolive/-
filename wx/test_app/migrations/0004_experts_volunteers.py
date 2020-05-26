# Generated by Django 2.2.6 on 2020-04-22 12:01

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0003_auto_20200422_1751'),
    ]

    operations = [
        migrations.CreateModel(
            name='Volunteers',
            fields=[
                ('myuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='test_app.MyUser')),
                ('patients', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_volunteers', to='test_app.MyUser')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('test_app.myuser',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Experts',
            fields=[
                ('myuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='test_app.MyUser')),
                ('patients', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_experts', to='test_app.MyUser')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('test_app.myuser',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
