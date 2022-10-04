from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'movies.core'
    verbose_name = 'core'

    def ready(self):
        import movies.core.signals

