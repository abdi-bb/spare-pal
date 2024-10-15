from django.shortcuts import render

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

    # def create(self, request, *args, **kwargs):
    #     data = request.data.copy() # Make mutable copy of request data
    #     supplier_id = data.pop('supplier_id', None)
    #     print(supplier_id)
    #     if supplier_id is None:
    #         return Response({"error": "supplier_id is required."}, status=status.HTTP_400_BAD_REQUEST)
        
    #     # Check if supplier_id is a list and take the first element
    #     if isinstance(supplier_id, list):
    #         if len(supplier_id) > 0:
    #             supplier_id = supplier_id[0]  # Take the first item from the list
    #         else:
    #             return Response({"error": "supplier_id cannot be an empty list."}, status=status.HTTP_400_BAD_REQUEST)
    #     try:
    #         # Attempt to typecast supplier_id to an integer
    #         supplier_id = int(supplier_id)
    #         supplier = Supplier.objects.get(id=supplier_id)
    #     except ValueError:
    #         return Response({"error": "supplier_id must be a valid integer."}, status=status.HTTP_400_BAD_REQUEST)
    #     except Supplier.DoesNotExist:
    #         return Response({"error": "Supplier not found."}, status=status.HTTP_404_NOT_FOUND)
        
    #     serializer = self.get_serializer(data=data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save(company=supplier)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)
    

class CompanyManagerDetailViewSet(viewsets.ModelViewSet):
    queryset = CompanyManagerDetail.objects.all()
    serializer_class = CompanyManagerDetailSerializer

    # def create(self, request, *args, **kwargs):
    #     data = request.data.copy() # Make mutable copy of request data
    #     supplier_id = data.pop('supplier_id', None)

    #     supplier_id = request.data.pop('supplier_id')
    #     if supplier_id is None:
    #         return Response({"error": "supplier_id is required."}, status=status.HTTP_400_BAD_REQUEST)
        
    #     # Check if supplier_id is a list and take the first element
    #     if isinstance(supplier_id, list):
    #         if len(supplier_id) > 0:
    #             supplier_id = supplier_id[0]  # Take the first item from the list
    #         else:
    #             return Response({"error": "supplier_id cannot be an empty list."}, status=status.HTTP_400_BAD_REQUEST)
    #     try:
    #         # Attempt to typecast supplier_id to an integer
    #         supplier_id = int(supplier_id)
    #         supplier = Supplier.objects.get(id=supplier_id)
    #     except ValueError:
    #         return Response({"error": "supplier_id must be a valid integer."}, status=status.HTTP_400_BAD_REQUEST)
    #     except Supplier.DoesNotExist:
    #         return Response({"error": "Supplier not found."}, status=status.HTTP_404_NOT_FOUND)
        
    #     serializer = self.get_serializer(data=data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save(company=supplier)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)