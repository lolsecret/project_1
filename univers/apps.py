from django.apps import AppConfig


class UniversConfig(AppConfig):
    name = 'univers'

    def ready(self):
        import univers.signals
