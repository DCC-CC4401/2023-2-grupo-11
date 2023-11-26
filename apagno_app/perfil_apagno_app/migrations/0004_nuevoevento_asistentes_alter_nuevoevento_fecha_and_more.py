# Generated by Django 4.1 on 2023-11-25 15:39

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("perfil_apagno_app", "0003_alter_nuevoevento_hora"),
    ]

    operations = [
        migrations.AddField(
            model_name="nuevoevento",
            name="asistentes",
            field=models.ManyToManyField(
                blank=True, related_name="eventos_asistir", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterField(
            model_name="nuevoevento",
            name="fecha",
            field=models.DateField(default="2023-11-25"),
        ),
        migrations.AlterField(
            model_name="nuevoevento",
            name="hora",
            field=models.TimeField(default="15:39"),
        ),
    ]