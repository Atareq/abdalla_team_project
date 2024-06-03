from django.urls import path, include
from .views import AdminShipmentViewSet, UserShipmentViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'shipment/admin', AdminShipmentViewSet,
                basename='shipmentuser')
router.register(r'shipment/user', UserShipmentViewset,
                basename='shipmentadmin')
urlpatterns = [
    path('', include(router.urls)),
]
