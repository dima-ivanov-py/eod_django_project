from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from core.urls import urlpatterns

urlpatterns.append(
    path(
        "token/",
        TokenObtainPairView.as_view(),
        name="token_obtain_pair",
    ),
)
