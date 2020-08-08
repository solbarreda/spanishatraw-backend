from django.contrib import admin

from .models import (
    Price,
    Invoice,
)

admin.site.register(Price)
admin.site.register(Invoice)
