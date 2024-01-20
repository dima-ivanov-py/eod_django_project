from django.urls import include, path

from core.urls import urlpatterns

urlpatterns.append(path("api/v1/", include("api.v1.urls")))
