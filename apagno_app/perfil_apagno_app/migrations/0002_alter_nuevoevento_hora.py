# Generated by Django 4.1 on 2023-11-01 01:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("perfil_apagno_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="nuevoevento",
            name="hora",
            field=models.TimeField(default="01:28"),
        ),
    ]
