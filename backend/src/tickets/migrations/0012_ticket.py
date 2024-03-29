# Generated by Django 5.0.1 on 2024-03-12 15:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0011_alter_registro_fecha_liquidaciones'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id_registro', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_liquidaciones', models.TextField(default=datetime.date.today)),
                ('usuario', models.CharField(max_length=100)),
                ('concepto', models.CharField(max_length=100)),
                ('empresa', models.CharField(max_length=100)),
                ('legajo', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=100)),
                ('observaciones', models.TextField(default=' ')),
                ('estado_liquidaciones', models.CharField(default='Pendiente', max_length=50)),
            ],
        ),
    ]
