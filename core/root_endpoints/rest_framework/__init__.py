from django.urls import include, path

from core.urls import urlpatterns

urlpatterns.append(
    path(
        "api-auth/",
        include(
            "rest_framework.urls",
            namespace="rest_framework",
        ),
    ),
)
