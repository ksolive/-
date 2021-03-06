# Generated by Django 2.2.6 on 2020-04-28 09:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('article', '0002_auto_20190403_2129'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('reviewText', models.TextField(default='')),
                ('picture', models.ImageField(blank=True, upload_to='picture/%Y%m%d/')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('questionID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='article.ArticlePost')),
                ('writerID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='write_review', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]
