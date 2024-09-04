# Generated by Django 5.0.7 on 2024-09-03 23:21

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bas', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='uc',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_requests_created', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='AlbumGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre del Álbum')),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='Descripción')),
                ('imagen', models.ImageField(upload_to='imagenes/album/', verbose_name='Imagen')),
                ('uc', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_requests_created', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ImageGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('titulo', models.CharField(max_length=100, verbose_name='Título de la Imagen')),
                ('imagen', models.ImageField(upload_to='imagenes/album/imagenes/', verbose_name='Imagen')),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='Descripción')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imagenes', to='bas.albumgallery', verbose_name='Álbum')),
                ('uc', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_requests_created', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]