# Generated by Django 4.0.6 on 2022-08-09 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_music_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='music',
            name='likes',
        ),
        migrations.AlterField(
            model_name='music',
            name='release_date',
            field=models.CharField(max_length=255),
        ),
    ]
