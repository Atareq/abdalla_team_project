from rest_framework import serializers
from .models import Shipments


class ShipmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipments
        fields = ['id', 'employee',
                  'approved', 'shipped', 'product_id', 'quentity']


class ShipmentsUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipments
        fields = ['id', 'approved', 'shipped', 'admin_approved']
