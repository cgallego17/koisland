# Generated by Django 5.0.7 on 2024-10-24 00:11

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0020_remove_seccionweb6_descripcionimg4_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_cliente', models.CharField(max_length=255)),
                ('contenido', models.TextField()),
                ('fecha_publicacion', models.DateTimeField(default=django.utils.timezone.now)),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='SeccionWeb7',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('breadcrumb', models.CharField(max_length=255)),
                ('titulo', models.CharField(max_length=255)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='bannerSeccion5/')),
                ('boton', models.CharField(max_length=255)),
                ('testimonio', models.ManyToManyField(related_name='testimonios', to='web.testimonio')),
            ],
        ),
    ]