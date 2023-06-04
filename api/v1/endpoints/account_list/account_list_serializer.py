from rest_framework import serializers

from dbmodels.models import Account


class AccountListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = (
            'id',
            'user',
            'type',
        )
        read_only_fields = fields

