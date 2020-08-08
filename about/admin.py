from django.contrib import admin

from .models import (
    Testimonial,
    ContactUs,
    Feature,
    EvidenceGallery,
)

admin.site.register(Testimonial)
admin.site.register(ContactUs)
admin.site.register(Feature)
admin.site.register(EvidenceGallery)
