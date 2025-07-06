from .models import Order
from django.utils import timezone
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import User

from rest_framework import serializers
from django.utils import timezone
from .models import Order
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import User

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = [
            'user', 
            'status', 
            'delivery_man', 
            'created_at', 
            'delivery_completed_at', 
            'payment_status'
        ]

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)


class AdminOrderUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['delivery_man', 'status', 'payment_status']


class DeliveryManOrderUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['status']

    def update(self, instance, validated_data):
        if validated_data.get('status') == 'complete' and not instance.delivery_completed_at:
            instance.delivery_completed_at = timezone.now()
        return super().update(instance, validated_data)

class AdminOrderUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['delivery_man', 'status']

class DeliveryManOrderUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['status']

    def update(self, instance, validated_data):
        if validated_data.get('status') == 'complete' and not instance.delivery_completed_at:
            instance.delivery_completed_at = timezone.now()
        return super().update(instance, validated_data)







class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    confirm_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['id','email','password', 'confirm_password','role']
        extra_kwargs = {
            'role': {'read_only': True},  # role set via admin only
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        user = User.objects.create_user(**validated_data)
        return user

