from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets, status
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
        supplier_id = request.data.pop('supplier_id')
        try:
            supplier = Supplier.objects.get(id=supplier_id)
        except Supplier.DoesNotExist:
            raise NotFound(detail="Supplier not found.")
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(company=supplier)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

class CompanyManagerDetailViewSet(viewsets.ModelViewSet):
    queryset = CompanyManagerDetail.objects.all()
    serializer_class = CompanyManagerDetailSerializer

    def create(self, request, *args, **kwargs):
        supplier_id = request.data.pop('supplier_id')
        try:
            supplier = Supplier.objects.get(id=supplier_id)
        except Supplier.DoesNotExist:
            raise NotFound(detail="Supplier not found.")
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(company=supplier)
        return Response(serializer.data, status=status.HTTP_201_CREATED)