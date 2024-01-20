from django.urls import path
from rest_framework_simplejwt.views import TokenVerifyView

from core.urls import urlpatterns

urlpatterns.append(
    path(
        "token/verify/",
        TokenVerifyView.as_view(),
        name="token_verify",
    ),
)
