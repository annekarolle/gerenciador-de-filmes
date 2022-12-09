# Generated by Django 4.1.4 on 2022-12-08 00:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0008_movie_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='user',
        ),
        migrations.AddField(
            model_name='movie',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='movie', to=settings.AUTH_USER_MODEL),
        ),
    ]
