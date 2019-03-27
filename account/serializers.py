from rest_framework import serializers


class AccountSerializer(serializers.Serializer):
    account_name = serializers.CharField()
    account_type = serializers.CharField()
    account_number = serializers.CharField()
    created_by = serializers.CharField()
    business_type = serializers.CharField()
    fund_source = serializers.CharField(allow_blank=True)
    beneficial_owner_info = serializers.CharField()

    passport_number = serializers.CharField(allow_blank=True)
    nid_number = serializers.CharField()
    tin_number = serializers.CharField(allow_blank=True)
    vat_reg_number = serializers.CharField(allow_blank=True)
    driving_licence_number = serializers.CharField(allow_blank=True)

    occupation = serializers.CharField()
    comments = serializers.CharField(required=False)


