from django.urls import path

from api.v1.get_something_1.get_something_view import GetSomething1View
from api.v1.urls import urlpatterns

urlpatterns.append(
    path(
        "get-something-1/",
        GetSomething1View.as_view(),
        name="get_something_1",
    )
)
