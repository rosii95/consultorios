# Generated by Django 5.0 on 2023-12-14 20:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='esp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30, verbose_name='nombre')),
            ],
            options={
                'verbose_name': 'especialización',
                'verbose_name_plural': 'especialidades',
                'db_table': 'esp',
            },
        ),
        migrations.AddField(
            model_name='doctores',
            name='especialidad',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.esp'),
        ),
    ]
