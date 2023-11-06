from django.apps import AppConfig


class PerfilApagnoAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'perfil_apagno_app'

    def ready(self):
        import perfil_apagno_app.signals
