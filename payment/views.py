"""Payments view."""

from django.utils.timezone import now
from django.db.transaction import atomic

from rest_framework import viewsets, status, mixins
from rest_framework.response import Response

from users.models import Customer
from services.models import Service

from .models import Invoice
from .invoice_serializer import InvoiceSerializer
from .serializers import PaymentSerializer


class InvoiceViewSet(viewsets.ModelViewSet):
    """
    API CRUD endpoint for invoice model.
    """

    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer


class PaymentViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    """View to register a payment and generate an invoice."""

    serializer_class = PaymentSerializer

    @atomic()
    def create_order(self, serializer):
        """
        Create invoice with payment information and service.

        :param data: [description]
        :type data: [type]
        """
        data = serializer.validated_data
        service: Service = data['service']
        customer: Customer = Customer.objects.get_or_create(
            email=data['email'])[0]
        invoice: Invoice = Invoice(
            charged_amount=service.price.amount,
            currency=service.price.currency,
            timestamp=now(),
            customer=customer,
        )
        invoice.save()
        invoice.service.add(service)
        serializer.validated_data['invoice_id'] = invoice.id
        serializer.save()

    def create(self, request, *args, **kwargs):
        """Register payment."""
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            self.create_order(serializer)
            return Response({
                'payment_id': serializer.validated_data['payment_id'],
                'status': serializer.validated_data['status'],
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
