# Generated by Django 5.0.7 on 2024-09-03 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagegallery',
            name='album',
        ),
        migrations.RemoveField(
            model_name='imagegallery',
            name='uc',
        ),
        migrations.DeleteModel(
            name='AlbumGallery',
        ),
        migrations.DeleteModel(
            name='ImageGallery',
        ),
    ]