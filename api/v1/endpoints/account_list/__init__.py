from api.v1.urls import router
from api.v1.endpoints.account_list.account_list_view import AccountListView

router.register(r'accounts', AccountListView, basename='accounts')

