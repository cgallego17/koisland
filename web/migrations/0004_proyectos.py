# Generated by Django 5.0.7 on 2024-10-23 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proyectos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('resultados', models.TextField(blank=True, null=True)),
                ('presupuesto', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('imagenes', models.ImageField(blank=True, null=True, upload_to='proyectos/')),
                ('archivos', models.FileField(blank=True, null=True, upload_to='proyectos/archivos/')),
            ],
            options={
                'ordering': ['fecha_fin'],
            },
        ),
    ]
