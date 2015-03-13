from django.apps import AppConfig


class ImagerProfileConfig(AppConfig):
    name = 'imager_profile'
    verbose_name = 'Imager Profile'

    def ready(self):
        from handlers import create_profile
