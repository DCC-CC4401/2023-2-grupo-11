# Generated by Django 4.1 on 2023-11-26 00:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("perfil_apagno_app", "0007_alter_nuevoevento_hora"),
    ]

    operations = [
        migrations.AlterField(
            model_name="nuevoevento",
            name="fecha",
            field=models.DateField(default="2023-11-26"),
        ),
        migrations.AlterField(
            model_name="nuevoevento",
            name="hora",
            field=models.TimeField(default="00:09"),
        ),
    ]
