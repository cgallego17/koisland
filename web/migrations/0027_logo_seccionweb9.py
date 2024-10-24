# Generated by Django 5.0.7 on 2024-10-24 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0026_seccionweb8_bg'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_empresa', models.CharField(max_length=255)),
                ('imagen', models.ImageField(upload_to='logos/')),
                ('url_empresa', models.URLField(blank=True, null=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='SeccionWeb9',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('breadcrumb', models.CharField(max_length=255)),
                ('titulo', models.CharField(max_length=255)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='seccion9/')),
                ('logo', models.ManyToManyField(related_name='logos', to='web.logo')),
            ],
        ),
    ]