from rest_framework.response import Response
from .serializer import ShipmentsSerializer, ShipmentsUpdateSerializer
from .models import Shipments
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from .premissions import ShipmentsAdminPermission, ShipmentsUserPermission


class AdminShipmentViewSet(viewsets.ModelViewSet):
    queryset = Shipments.objects.all()
    serializer_class = ShipmentsSerializer
    permission_classes = [IsAuthenticated, ShipmentsAdminPermission]

    def list(self, request):
        queryset = self.get_queryset()
        shipment_serialized = ShipmentsSerializer(instance=queryset, many=True)
        return Response(shipment_serialized.data, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        shipment_serialized = ShipmentsSerializer(instance=instance)
        return Response(shipment_serialized.data, status=status.HTTP_200_OK)

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.approved:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
        instance.admin_approved = request.user
        serializer = ShipmentsUpdateSerializer(instance,
                                               data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({'Message': 'Deleted Sucessfuly'},
                        status=status.HTTP_200_OK)


class UserShipmentViewset(viewsets.ModelViewSet):
    queryset = Shipments.objects.all()
    serializer_class = ShipmentsSerializer
    permission_classes = [IsAuthenticated, ShipmentsUserPermission]

    def list(self, request):
        queryset = self.get_queryset().filter(employee=request.user)
        print('tarreeqqq')
        shipment_serialized = ShipmentsSerializer(instance=queryset, many=True)
        return Response(shipment_serialized.data, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if not instance.employee == request.user:
            return Response(status=status.HTTP_404_NOT_FOUND)
        shipment_serialized = ShipmentsSerializer(instance=instance)
        return Response(shipment_serialized.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        shipment_data = request.data.copy()
        shipment_data["employee"] = request.user.id
        serializer = ShipmentsSerializer(data=shipment_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
