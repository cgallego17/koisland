# Generated by Django 5.0.7 on 2024-10-23 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0013_seccionweb3_remove_seccionweb2_contador1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='seccionweb3',
            name='contadorImg1',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='seccionweb3',
            name='contadorImg2',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='seccionweb3',
            name='contadorImg3',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='seccionweb3',
            name='contadorImg4',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='seccionweb3',
            name='tituloImg1',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='seccionweb3',
            name='tituloImg2',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='seccionweb3',
            name='tituloImg3',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='seccionweb3',
            name='tituloImg4',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
