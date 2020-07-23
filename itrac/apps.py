from django.apps import AppConfig


class iTracConfig(AppConfig):
    name = 'itrac'

    def ready(self):
        import itrac.signals
