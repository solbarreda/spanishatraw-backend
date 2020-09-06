"""Payment admin."""

from django.contrib import admin

from spanishatraw.admin import ReadOnlyAdminMixin
from .models import (
    Price,
    Invoice,
    Payment,
)


@admin.register(Payment)
class PaymentAdmin(ReadOnlyAdminMixin):
    """Payment admin."""

    pass


@admin.register(Invoice)
class InvoiceAdmin(ReadOnlyAdminMixin):
    """Payment admin."""

    pass


admin.site.register(Price)
