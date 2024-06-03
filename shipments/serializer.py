from rest_framework import serializers
from .models import Shipments


class ShipmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipments
        fields = ['id', 'employee', 'date_time',
                  'approved', 'shipped', 'product_id']
