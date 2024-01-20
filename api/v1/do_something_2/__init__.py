from django.urls import path

from api.v1.do_something_2.do_something_2_view import DoSomething2View
from api.v1.urls import urlpatterns

urlpatterns.append(
    path(
        "do-something-2/",
        DoSomething2View.as_view(),
        name="do_something_2",
    )
)
