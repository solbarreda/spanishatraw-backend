from rest_framework import serializers

from users.serializers import UserSerializer
from services.serializers import ServiceSerializer
from .models import (
    Invoice,
)


class InvoiceSerializer(serializers.ModelSerializer):
    """Invoice serializer."""

    # service = ServiceSerializer()
    # user = UserSerializer()

    class Meta:
        model = Invoice
        fields = ['id', 'service', 'charged_amount', 'timestamp', 'user', ]
