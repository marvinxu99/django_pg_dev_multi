from django.apps import AppConfig


class iTracConfig(AppConfig):
    name = 'itrac'
    verbose_name = "Issue Tracker"

    def ready(self):
        import itrac.signals
