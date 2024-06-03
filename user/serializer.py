from rest_framework import serializers
from .models import CustomUser


class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'userimage', 'phonenumber',
                  'employee_id', 'is_admin']


class SignInSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(style={'input_type': 'password'})

    class Meta:
        model = CustomUser
        fields = ['username', 'password']
