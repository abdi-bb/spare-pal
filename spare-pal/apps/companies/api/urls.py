from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet, CompanyDetailAddressViewSet, CompanyManagerDetailViewSet, GetChoicesAPIView

company_router = DefaultRouter()
company_router.register(r'companies', CompanyViewSet)
company_router.register(r'company-detail-address', CompanyDetailAddressViewSet)
company_router.register(r'company-manager-detail', CompanyManagerDetailViewSet)

urlpatterns = [
    path('choices/', GetChoicesAPIView.as_view(), name='get_choices'),
]