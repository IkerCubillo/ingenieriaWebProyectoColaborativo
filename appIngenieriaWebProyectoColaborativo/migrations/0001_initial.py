# Generated by Django 4.2.16 on 2024-11-11 12:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Raza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='SubRaza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=2000)),
                ('raza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appIngenieriaWebProyectoColaborativo.raza')),
            ],
        ),
        migrations.CreateModel(
            name='Personaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('edadTierra', models.CharField(max_length=50)),
                ('fecha_nacimiento', models.DateField()),
                ('fecha_muerte', models.DateField()),
                ('genero', models.CharField(max_length=50)),
                ('antiguedad', models.IntegerField(default=0)),
                ('peliculas', models.ManyToManyField(to='appIngenieriaWebProyectoColaborativo.pelicula')),
                ('raza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appIngenieriaWebProyectoColaborativo.raza')),
                ('subRaza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appIngenieriaWebProyectoColaborativo.subraza')),
            ],
        ),
    ]
