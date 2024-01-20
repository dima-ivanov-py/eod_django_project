from django.urls import path

from api.v1.do_something_1.do_something_1_view import DoSomething1View
from api.v1.urls import urlpatterns

urlpatterns.append(
    path(
        "do-something-1/",
        DoSomething1View.as_view(),
        name="do_something_1",
    )
)
