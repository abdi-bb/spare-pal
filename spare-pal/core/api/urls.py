from django.urls import path, include
from rest_framework.routers import DefaultRouter
from suppliers.api.urls import supplier_router

router = DefaultRouter()
router.registry.extend(supplier_router.registry)

urlpatterns = [
    path('', include(router.urls)),
]