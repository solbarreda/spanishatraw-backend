from rest_framework import serializers

from payment.serializers import PriceSerializer
from .models import (
    Service,
    AgeRange,
    Homework,
)


class AgeRangeSerializer(serializers.ModelSerializer):
    """Age Range serializer."""

    class Meta:
        model = AgeRange
        fields = ['id', 'min', 'max', ]


class ServiceSerializer(serializers.ModelSerializer):
    """Service serializer."""

    price = PriceSerializer()
    age_range = AgeRangeSerializer()

    class Meta:
        model = Service
        fields = [
            'id', 'name', 'timestamp', 'image', 'schedule', 'price', 'age_range', ]


class HomeworkSerializer(serializers.ModelSerializer):
    """Homework serializer."""

    service = ServiceSerializer()

    class Meta:
        model = Homework
        fields = ['id', 'file', 'description', 'name', 'service', ]
