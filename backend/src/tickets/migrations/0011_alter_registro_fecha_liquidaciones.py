# Generated by Django 5.0.3 on 2024-03-08 16:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0010_alter_registro_fecha_liquidaciones'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registro',
            name='fecha_liquidaciones',
            field=models.TextField(default=datetime.date.today),
        ),
    ]
