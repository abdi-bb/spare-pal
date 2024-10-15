from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SupplierViewSet, CompanyDetailAddressViewSet, CompanyManagerDetailViewSet

supplier_router = DefaultRouter()
supplier_router.register(r'suppliers', SupplierViewSet)
supplier_router.register(r'company-detail-address', CompanyDetailAddressViewSet)
supplier_router.register(r'company-manager-detail', CompanyManagerDetailViewSet)
