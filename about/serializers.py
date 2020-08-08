from rest_framework import serializers

from users.serializers import UserSerializer
from .models import (
    Testimonial,
    ContactUs,
    Feature,
    EvidenceGallery,
)


class TestimonialSerializer(serializers.ModelSerializer):
    """Testimonial serializer."""

    user = UserSerializer()

    class Meta:
        model = Testimonial
        fields = ['id', 'user', 'timestamp', 'content', ]


class ContactUsSerializer(serializers.ModelSerializer):
    """ContactUs serializer."""

    user = UserSerializer()

    class Meta:
        model = ContactUs
        fields = ['id', 'user', 'description', 'subject', ]


class FeatureSerializer(serializers.ModelSerializer):
    """Feature serializer."""

    class Meta:
        model = Feature
        fields = ['id', 'name', 'description', ]


class EvidenceGallerySerializer(serializers.ModelSerializer):
    """EvidenceGallery serializer."""

    class Meta:
        model = EvidenceGallery
        fields = ['id', 'name', 'description', 'image', ]
