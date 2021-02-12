from django.apps import AppConfig


class iTracConfig(AppConfig):
    name = 'itrac'
    verbose_name = "Issue Tracker"

    # App specific settings:

    def ready(self):
        import itrac.signals     # noqa
