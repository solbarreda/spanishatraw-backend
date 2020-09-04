"""Serializers."""
from rest_framework import serializers

from .models import (
    Payment,
)
from services.models import (
    Service,
)


class PaymentSerializer(serializers.ModelSerializer):
    """PayPal data validator."""

    service = serializers.PrimaryKeyRelatedField(
        queryset=Service.objects.all())
    email = serializers.EmailField()

    class Meta:
        model = Payment
        fields = [
            'response_data', 'gateway', 'status', 'payment_id', 'service',
            'email']

    def create(self, validated_data):
        del validated_data['email']
        del validated_data['service']
        return super().create(validated_data)
