# Generated by Django 4.1 on 2023-11-27 03:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("perfil_apagno_app", "0016_alter_nuevoevento_hora"),
    ]

    operations = [
        migrations.AlterField(
            model_name="nuevoevento",
            name="hora",
            field=models.TimeField(default="03:24"),
        ),
    ]
