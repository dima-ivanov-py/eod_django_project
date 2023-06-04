from django.apps import AppConfig


class V1Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api.v1'

    def ready(self):
        import api.v1.endpoints
        from api.v1.urls import urlpatterns, router
        from django.urls import path, include

        urlpatterns.append(path('', include(router.urls)))

        return super().ready()

