from rest_framework import serializers
from suppliers.models import Supplier, CompanyDetailAddress, CompanyManagerDetail


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = [
            'company_name', 'date_registered', 'tin_number', 'renewed_license_date',
            'license_number', 'legal_status', 'code', 'business_description',
            'sub_group_code', 'sub_group_description'
        ]


class CompanyDetailAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyDetailAddress
        fields = '__all__'

class CompanyManagerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyManagerDetail
        fields = '__all__'
