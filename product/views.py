from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Product
from .serializer import ProductSerializer
from .permissions import ProductPermission
from django.shortcuts import get_object_or_404


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, ProductPermission]

    def create(self, request, *args, **kwargs):
        product_data = request.data.copy()
        product_data["employee"] = request.user.id
        serializer = self.get_serializer(data=product_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, *args, **kwargs):
        product = get_object_or_404(Product, id=kwargs['pk'])
        product_serialized = ProductSerializer(instance=product)
        return Response(product_serialized.data, status=status.HTTP_200_OK)

    def list(self, request):
        queryset = Product.objects.all()
        Product_serialized = ProductSerializer(instance=queryset, many=True)
        return Response(Product_serialized.data, status=status.HTTP_200_OK)

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = ProductSerializer(instance, data=request.data,
                                       partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({'Message': 'Deleted Sucessfuly'},
                        status=status.HTTP_200_OK)
