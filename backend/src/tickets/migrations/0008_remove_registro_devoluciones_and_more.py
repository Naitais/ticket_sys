# Generated by Django 5.0.3 on 2024-03-08 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0007_rename_operador_liquidaciones_registro_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registro',
            name='devoluciones',
        ),
        migrations.RemoveField(
            model_name='registro',
            name='estado_sistemas',
        ),
        migrations.RemoveField(
            model_name='registro',
            name='fecha_sistemas',
        ),
        migrations.RemoveField(
            model_name='registro',
            name='operador_sistemas',
        ),
        migrations.AlterField(
            model_name='registro',
            name='estado_liquidaciones',
            field=models.CharField(default='Pendiente', max_length=50),
        ),
    ]
