# Generated by Django 5.0.1 on 2024-02-08 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0002_prueba'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id_registro', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_liquidaciones', models.DateField()),
                ('operador_liquidaciones', models.CharField(max_length=100)),
                ('concepto', models.CharField(max_length=100)),
                ('empresa', models.CharField(max_length=100)),
                ('legajo', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=100)),
                ('observaciones', models.TextField()),
                ('estado_liquidaciones', models.CharField(max_length=50)),
                ('operador_sistemas', models.CharField(max_length=100)),
                ('estado_sistemas', models.CharField(max_length=50)),
                ('devoluciones', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha_sistemas', models.DateField()),
            ],
        ),
    ]