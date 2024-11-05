from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.suppliers.api.urls import supplier_router

router = DefaultRouter()
router.registry.extend(supplier_router.registry)

urlpatterns = [
    path('', include(router.urls)),
    # Add this to include non-router paths like `choices/`
    path('', include('apps.suppliers.api.urls')),  # Include the suppliers' URLs to handle choices/
]