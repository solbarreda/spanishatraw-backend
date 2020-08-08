from rest_framework import serializers

from .models import Service, AgeRange, Homework


class ServiceSerializer(serializers.ModelSerializer):
    """Service serializer."""

    class Meta:
        model = Service
        fields = [
            'id', 'name', 'timestamp', 'image', 'schedule', 'price', 'age_range', ]


class AgeRangeSerializer(serializers.ModelSerializer):
    """Age Range serializer."""

    class Meta:
        model = AgeRange
        fields = ['id', 'min', 'max', ]


class HomeworkSerializer(serializers.ModelSerializer):
    """Homework serializer."""

    class Meta:
        model = Homework
        fields = ['id', 'file', 'description', 'name', 'service', ]
