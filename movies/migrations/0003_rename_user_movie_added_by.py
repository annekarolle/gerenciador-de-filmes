# Generated by Django 4.1.4 on 2022-12-07 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_alter_movie_duration'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='user',
            new_name='added_by',
        ),
    ]
