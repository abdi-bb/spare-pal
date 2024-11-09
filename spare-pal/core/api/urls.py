from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.companies.api.urls import company_router

router = DefaultRouter()
router.registry.extend(company_router.registry)

urlpatterns = [
    path('', include(router.urls)),
    # Add this to include non-router paths like `choices/`
    path('', include('apps.companies.api.urls')),  # Include the suppliers' URLs to handle choices/
    path('auth/', include('apps.accounts.api.urls')),
]