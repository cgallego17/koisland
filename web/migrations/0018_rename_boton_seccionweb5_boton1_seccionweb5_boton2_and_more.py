# Generated by Django 5.0.7 on 2024-10-23 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0017_seccionweb5_alter_seccionweb3_imagen1_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='seccionweb5',
            old_name='boton',
            new_name='boton1',
        ),
        migrations.AddField(
            model_name='seccionweb5',
            name='boton2',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='seccionweb5',
            name='boton3',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
