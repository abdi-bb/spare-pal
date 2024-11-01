from rest_framework import serializers
from apps.suppliers.models import Supplier, CompanyDetailAddress, CompanyManagerDetail


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = [
            'id', 'company_name', 'date_registered', 'tin_number',
            'renewed_license_date', 'license_number', 'legal_status', 'code',
            'business_description', 'sub_group_code', 'sub_group_description'
        ]


class CompanyDetailAddressSerializer(serializers.ModelSerializer):
    company = serializers.CharField(read_only=True)
    company_id = serializers.CharField(source='company.id', read_only=True)


    class Meta:
        model = CompanyDetailAddress
        fields = '__all__'

class CompanyManagerDetailSerializer(serializers.ModelSerializer):
    company = serializers.CharField(read_only=True)
    company_id = serializers.CharField(source='company.id', read_only=True)

    
    class Meta:
        model = CompanyManagerDetail
        fields = '__all__'
