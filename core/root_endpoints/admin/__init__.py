from django.contrib import admin
from django.urls import path

from core.urls import urlpatterns

urlpatterns.append(path("admin/", admin.site.urls))
