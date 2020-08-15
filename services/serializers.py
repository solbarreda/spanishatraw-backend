"""Services serializer."""
from rest_framework import serializers

from payment.serializers import PriceSerializer
from .models import (
    Service,
    GradeRange,
    Homework,
    ServiceLevel,
    ServiceType,
)


class ServiceTypeSerializer(serializers.ModelSerializer):
    """Service type serializer."""

    class Meta:
        model = ServiceType
        fields = ['id', 'description', ]


class ServiceLevelSerializer(serializers.ModelSerializer):
    """Service level serializer."""

    class Meta:
        model = ServiceLevel
        fields = ['id', 'description', ]


class GradeRangeSerializer(serializers.ModelSerializer):
    """Age Range serializer."""

    class Meta:
        model = GradeRange
        fields = ['id', 'min', 'max', ]


class ServiceSerializer(serializers.ModelSerializer):
    """Service serializer."""

    price = PriceSerializer()
    grade_range = GradeRangeSerializer()
    level = ServiceLevelSerializer()
    type = ServiceTypeSerializer()

    class Meta:
        model = Service
        fields = [
            'id', 'name', 'timestamp', 'image', 'schedule', 'price',
            'grade_range', 'level', 'type']


class HomeworkSerializer(serializers.ModelSerializer):
    """Homework serializer."""

    service = ServiceSerializer()

    class Meta:
        model = Homework
        fields = ['id', 'file', 'description', 'name', 'service', ]
