# Generated by Django 5.0.7 on 2024-10-23 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_alter_seccionweb1_titulodescripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seccionweb1',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='seccion1/'),
        ),
    ]