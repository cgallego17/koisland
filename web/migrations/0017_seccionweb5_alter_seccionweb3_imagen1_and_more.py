# Generated by Django 5.0.7 on 2024-10-23 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0016_seccionweb4'),
    ]

    operations = [
        migrations.CreateModel(
            name='SeccionWeb5',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('breadcrumb', models.CharField(max_length=255)),
                ('titulo', models.CharField(max_length=255)),
                ('imagen1', models.ImageField(blank=True, null=True, upload_to='bannerSeccion5/')),
                ('imagen2', models.ImageField(blank=True, null=True, upload_to='bannerSeccion5/')),
                ('imageCard1', models.ImageField(blank=True, null=True, upload_to='bannerSeccion5/')),
                ('tituloCard1', models.CharField(max_length=255)),
                ('precioCard1', models.IntegerField()),
                ('imageCard2', models.ImageField(blank=True, null=True, upload_to='bannerSeccion5/')),
                ('tituloCard2', models.CharField(max_length=255)),
                ('precioCard2', models.IntegerField()),
                ('imageCard3', models.ImageField(blank=True, null=True, upload_to='bannerSeccion5/')),
                ('tituloCard3', models.CharField(max_length=255)),
                ('precioCard3', models.IntegerField()),
                ('boton', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='seccionweb3',
            name='imagen1',
            field=models.ImageField(blank=True, null=True, upload_to='bannerSeccion4/'),
        ),
        migrations.AlterField(
            model_name='seccionweb3',
            name='imagen2',
            field=models.ImageField(blank=True, null=True, upload_to='bannerSeccion4/'),
        ),
        migrations.AlterField(
            model_name='seccionweb3',
            name='imagen3',
            field=models.ImageField(blank=True, null=True, upload_to='bannerSeccion4/'),
        ),
        migrations.AlterField(
            model_name='seccionweb3',
            name='imagen4',
            field=models.ImageField(blank=True, null=True, upload_to='bannerSeccion4/'),
        ),
    ]
