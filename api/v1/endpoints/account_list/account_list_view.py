from rest_framework.generics import ListAPIView
from rest_framework.viewsets import GenericViewSet, ViewSetMixin
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated

from dbmodels.models import Account
from api.v1.endpoints.account_list.account_list_serializer import (
    AccountListSerializer,
)


class AccountListView(ViewSetMixin, ListAPIView):
    serializer_class = AccountListSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Account.objects.filter(user=self.request.user)

