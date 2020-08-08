from rest_framework import serializers

from .models import (
    Price,
)


class PriceSerializer(serializers.ModelSerializer):
    """Price serializer."""

    class Meta:
        model = Price
        fields = ['id', 'amount', 'currency']
