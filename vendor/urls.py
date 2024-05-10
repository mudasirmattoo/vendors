from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VendorViewSet, VendorPerformanceViewSet, PurchaseOrderViewSet

router = DefaultRouter()
router.register(r'vendors', VendorViewSet)
router.register(r'purchase_orders', PurchaseOrderViewSet)
router.register(r'vendor-performance', VendorPerformanceViewSet, basename='vendor-performance')

urlpatterns = [
    path('api/', include(router.urls)),
]
