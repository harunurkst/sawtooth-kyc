from rest_framework import serializers


class AccountSerializer(serializers.Serializer):
    account_number = serializers.CharField()
    account_name = serializers.CharField()
    balance = serializers.CharField()