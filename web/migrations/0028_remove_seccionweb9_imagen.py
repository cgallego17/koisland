# Generated by Django 5.0.7 on 2024-10-24 01:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0027_logo_seccionweb9'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seccionweb9',
            name='imagen',
        ),
    ]