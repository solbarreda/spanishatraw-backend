from django.contrib import admin

from .models import (
    Service,
    Homework,
    GradeRange,
    ServiceLevel,
    ServiceType,
)

admin.site.register(Service)
admin.site.register(Homework)
admin.site.register(GradeRange)
admin.site.register(ServiceLevel)
admin.site.register(ServiceType)
