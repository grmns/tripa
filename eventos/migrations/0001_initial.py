# Generated by Django 5.0.6 on 2024-06-13 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('fecha_inicio', models.DateTimeField()),
                ('fecha_fin', models.DateTimeField()),
                ('ubicacion', models.CharField(max_length=200)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='imagenes_eventos/', verbose_name='Imagen')),
            ],
        ),
    ]
