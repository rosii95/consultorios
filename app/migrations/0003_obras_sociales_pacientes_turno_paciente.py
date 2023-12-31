# Generated by Django 5.0 on 2023-12-15 18:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_esp_doctores_especialidad'),
    ]

    operations = [
        migrations.CreateModel(
            name='obras_sociales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30, verbose_name='nombre')),
                ('detalle', models.CharField(max_length=100, verbose_name='detalle')),
            ],
            options={
                'verbose_name': 'os',
                'verbose_name_plural': 'obras socialas',
                'db_table': 'os',
            },
        ),
        migrations.CreateModel(
            name='pacientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dni', models.CharField(max_length=8, verbose_name='DNI')),
                ('nombre', models.CharField(max_length=30, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=30, verbose_name='Apellido')),
            ],
            options={
                'verbose_name': 'paciente',
                'verbose_name_plural': 'pacientes',
                'db_table': 'pacientes',
            },
        ),
        migrations.AddField(
            model_name='turno',
            name='paciente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.pacientes'),
        ),
    ]
