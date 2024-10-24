from django.shortcuts import get_object_or_404, render

# Create your views here.

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from suppliers.models import Supplier, CompanyDetailAddress, CompanyManagerDetail
from .serializers import SupplierSerializer, CompanyDetailAddressSerializer, CompanyManagerDetailSerializer

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class CompanyDetailAddressViewSet(viewsets.ModelViewSet):
    queryset = CompanyDetailAddress.objects.all()
    serializer_class = CompanyDetailAddressSerializer

    def create(self, request, *args, **kwargs):
        data = request.data.copy()  # Make mutable copy of request data
        company_id = data.pop('company_id', None)

        if company_id is None:
            return Response({"error": "company_id is required."}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            company_id = int(company_id)
        except ValueError:
            return Response({"error": "company_id must be a valid integer."}, status=status.HTTP_400_BAD_REQUEST)

        company = get_object_or_404(Supplier, id=company_id)
        
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(company=company)  # Link the address to the company
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

class CompanyManagerDetailViewSet(viewsets.ModelViewSet):
    queryset = CompanyManagerDetail.objects.all()
    serializer_class = CompanyManagerDetailSerializer

    def create(self, request, *args, **kwargs):
        data = request.data.copy()  # Make mutable copy of request data
        company_id = data.pop('company_id', None)

        if company_id is None:
            return Response({"error": "company_id is required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            company_id = int(company_id)
        except ValueError:
            return Response({"error": "company_id must be a valid integer."}, status=status.HTTP_400_BAD_REQUEST)

        company = get_object_or_404(Supplier, id=company_id)

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(company=company)  # Link the manager to the company
        return Response(serializer.data, status=status.HTTP_201_CREATED)



# Django API Endpoint to Serve Choices
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from drf_spectacular.utils import extend_schema

from suppliers.models import (
LEGAL_STATUS_CHOICES,
BUSINESS_DESCRIPTION_CHOICES,
SUB_GROUP_DESCRIPTION_CHOICES,
REGION_CHOICES,
ZONE_CHOICES,
WOREDA_CHOICES,
KEBELE_CHOICES,
SITE_ID_CHOICES
)

@extend_schema(
    responses={
        200: {
            'type': 'object',
            'properties': {
                'legal_status': {'type': 'array', 'items': {'type': 'string'}},
                'business_description': {'type': 'array', 'items': {'type': 'string'}},
                'sub_group_description': {'type': 'array', 'items': {'type': 'string'}},
                'region': {'type': 'array', 'items': {'type': 'string'}},
                'zone': {'type': 'array', 'items': {'type': 'string'}},
                'woreda': {'type': 'array', 'items': {'type': 'string'}},
                'kebele': {'type': 'array', 'items': {'type': 'string'}},
                'site_id': {'type': 'array', 'items': {'type': 'string'}},
            }
        }
    }
)
class GetChoicesAPIView(APIView):
    def get(self, request):
        choices = {
            'legal_status': LEGAL_STATUS_CHOICES,
            'business_description': BUSINESS_DESCRIPTION_CHOICES,
            'sub_group_description': SUB_GROUP_DESCRIPTION_CHOICES,
            'region': REGION_CHOICES,
            'zone': ZONE_CHOICES,
            'woreda': WOREDA_CHOICES,
            'kebele': KEBELE_CHOICES,
            'site_id': SITE_ID_CHOICES
        }

        return Response(choices, status=status.HTTP_200_OK)