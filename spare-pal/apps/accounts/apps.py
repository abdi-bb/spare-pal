from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.accounts'

    # import signals
    def ready(self):
        import apps.accounts.api.signals # noqa