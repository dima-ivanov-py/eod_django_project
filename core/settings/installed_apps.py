INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # -------------------------
    "core.root_endpoints.apps.RootEndpointsConfig",
    "dbmodels.apps.DbmodelsConfig",
    "api.v1.apps.V1Config",
    # -------------------------
    "rest_framework",
    "rest_framework_simplejwt",
    "drf_yasg",
]
