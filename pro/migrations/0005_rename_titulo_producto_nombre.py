# Generated by Django 5.0.7 on 2024-08-28 00:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pro', '0004_producto_sku'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='titulo',
            new_name='nombre',
        ),
    ]
