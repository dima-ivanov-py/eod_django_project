from api.v1.urls import router
from api.v1.endpoints.users.user_view import UserView

router.register(r'users', UserView)

