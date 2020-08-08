from rest_framework import viewsets
from rest_framework import permissions

from .models import (
    Testimonial,
    ContactUs,
    Feature,
    EvidenceGallery,
)
from .serializers import (
    TestimonialSerializer,
    ContactUsSerializer,
    FeatureSerializer,
    EvidenceGallerySerializer,
)


class TestimonialViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that serves testimonials to be viewed only.
    """

    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer
    permission_classes = [permissions.IsAuthenticated]


class ContactUsViewSet(viewsets.ModelViewSet):
    """
    API CRUD endpoint for contact us model.
    """

    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer
    permission_classes = [permissions.IsAuthenticated]


class FeatureViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that serves features to be viewed only.
    """

    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer
    permission_classes = [permissions.IsAuthenticated]


class EvidenceGalleryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that serves Evidences Galleries to be viewed only.
    """

    queryset = EvidenceGallery.objects.all()
    serializer_class = EvidenceGallerySerializer
    permission_classes = [permissions.IsAuthenticated]
