# Generated by Django 5.0.7 on 2024-10-23 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0019_seccionweb6'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seccionweb6',
            name='descripcionImg4',
        ),
        migrations.AddField(
            model_name='seccionweb6',
            name='descripcion',
            field=models.TextField(blank=True, null=True),
        ),
    ]
