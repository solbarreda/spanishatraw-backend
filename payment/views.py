from rest_framework import viewsets
from rest_framework import permissions

from .models import (
    Invoice,
)
from .invoice_serializer import (
    InvoiceSerializer,
)


class InvoiceViewSet(viewsets.ModelViewSet):
    """
    API CRUD endpoint for invoice model.
    """

    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
