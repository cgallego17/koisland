# Generated by Django 5.0.7 on 2024-10-23 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0011_remove_seccionweb2_categorias_seccionweb2_categorias'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seccionweb2',
            name='categorias',
        ),
        migrations.RemoveField(
            model_name='seccionweb2',
            name='tituloDescripcion',
        ),
        migrations.AddField(
            model_name='seccionweb2',
            name='contador1',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='seccionweb2',
            name='contador2',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='seccionweb2',
            name='contador3',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='seccionweb2',
            name='imagen1',
            field=models.ImageField(blank=True, null=True, upload_to='seccion3/'),
        ),
        migrations.AddField(
            model_name='seccionweb2',
            name='imagen2',
            field=models.ImageField(blank=True, null=True, upload_to='seccion3/'),
        ),
        migrations.AddField(
            model_name='seccionweb2',
            name='imagen3',
            field=models.ImageField(blank=True, null=True, upload_to='seccion3/'),
        ),
        migrations.AddField(
            model_name='seccionweb2',
            name='imagen4',
            field=models.ImageField(blank=True, null=True, upload_to='seccion3/'),
        ),
        migrations.AddField(
            model_name='seccionweb2',
            name='tituloContador1',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='seccionweb2',
            name='tituloContador2',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='seccionweb2',
            name='tituloContador3',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]