from django.urls import include, path
from rest_framework import routers

from .views import (
    ContactUsViewSet,
    EvidenceGalleryViewSet,
    FeatureViewSet,
    TestimonialViewSet,
)

router = routers.DefaultRouter()
router.register(r'contact-us', ContactUsViewSet, basename='contact-us')
router.register(r'evidence-gallery', EvidenceGalleryViewSet,
                basename='evidence-gallery')
router.register(r'feature', FeatureViewSet, basename='feature')
router.register(r'testimonial', TestimonialViewSet, basename='testimonial')

urlpatterns = [
    path('', include(router.urls)),
]
