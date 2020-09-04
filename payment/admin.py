"""Payment admin."""

from django.contrib import admin

from spanishatraw.admin import ReadOnlyAdminMixin
from .models import (
    Price,
    Invoice,
    Payment,
)

admin.site.register(Price)
admin.site.register(Invoice)


admin.site.register(Payment)
# @admin.register(Payment)
# class Payment(ReadOnlyAdminMixin):
#     """Payment admin."""

#     pass
