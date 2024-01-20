from django.apps import AppConfig


class RootEndpointsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core.root_endpoints"

    def ready(self):
        import core.root_endpoints.endpoints

        return super().ready()
