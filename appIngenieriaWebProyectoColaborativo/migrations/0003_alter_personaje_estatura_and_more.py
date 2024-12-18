# Generated by Django 5.1.3 on 2024-11-17 22:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appIngenieriaWebProyectoColaborativo', '0002_remove_personaje_antiguedad_personaje_estatura_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personaje',
            name='estatura',
            field=models.FloatField(default=1.8),
        ),
        migrations.AlterField(
            model_name='personaje',
            name='fecha_muerte',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='personaje',
            name='subRaza',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='appIngenieriaWebProyectoColaborativo.subraza'),
        ),
    ]
