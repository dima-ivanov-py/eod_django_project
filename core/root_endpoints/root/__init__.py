from django.shortcuts import redirect
from django.urls import path

from core.urls import urlpatterns

urlpatterns.append(path("", lambda r: redirect("schema-swagger-ui")))
