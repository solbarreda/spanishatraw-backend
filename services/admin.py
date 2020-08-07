from django.contrib import admin

from .models import (
    Service,
    Homework,
    AgeRange,
)

admin.site.register(Service)
admin.site.register(Homework)
admin.site.register(AgeRange)
