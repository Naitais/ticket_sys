# Generated by Django 5.0.1 on 2024-03-12 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0012_ticket'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticket',
            old_name='id_registro',
            new_name='id_ticket',
        ),
    ]
