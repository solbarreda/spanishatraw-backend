"""Payment models."""

from django.db import models

from users.models import Customer

from .constants import (
    PAYMENT_GATEWAYS,
    PAYPAL,
    PAYMENT_STATUS,
    PENDING_STATUS,
)


class Price(models.Model):
    """
    Prices model.

    :cvar amount: Price amount.
    :cvar currency: Price currency.
    """

    USD_OPTION = 'USD'
    CURRENCY_OPTIONS = [
        ('USD', USD_OPTION)
    ]

    amount = models.DecimalField(
        verbose_name='Price amount', max_digits=8, decimal_places=2)
    currency = models.CharField(
        verbose_name='Currency', max_length=3, choices=CURRENCY_OPTIONS,
        default=USD_OPTION)

    class Meta:
        verbose_name = 'Price'
        verbose_name_plural = 'Prices'

    def __str__(self):
        """Price name."""
        return f'{self.currency} {self.amount}'


class Invoice(models.Model):
    """
    Invoice model

    :cvar service: Service related.
    :cvar charged_amount: Amount to charge.
    :cvar timestamp: Invoice time of creation.
    :cvar user: User related to the invoice.
    """

    service = models.ForeignKey(
        verbose_name='Invoice', to='services.Service', on_delete=models.DO_NOTHING)
    charged_amount = models.DecimalField(
        verbose_name='Charged amount', max_digits=8, decimal_places=2)
    currency = models.CharField(verbose_name='Currency', max_length=3)
    timestamp = models.DateTimeField(
        verbose_name='Timestamp', auto_now_add=True, null=False)
    customer = models.ForeignKey(
        verbose_name='Customer', to=Customer, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = 'Invoice'
        verbose_name_plural = 'Invoices'

    def __str__(self):
        """Invoice name."""
        return f'{self.customer.email} - {self.service}'


class Payment(models.Model):
    """
    Payment model to store payment metadata.

    :cvar response_data: JSONField, response information from the payment gateway.
    :cvar gateway: CharField, gateway to use.
    :cvar status: CharField, payment status.
    :cvar payment_id: CharField, payment id.
    :cvar invoice: OneToOneField, invoice related to the payment.
    """

    response_data = models.JSONField(verbose_name='Response data')
    gateway = models.CharField(
        verbose_name='Gateway', max_length=16, choices=PAYMENT_GATEWAYS,
        default=PAYPAL)
    status = models.CharField(
        verbose_name='Status', max_length=16, choices=PAYMENT_STATUS,
        default=PENDING_STATUS)
    payment_id = models.CharField(
        verbose_name='Payment ID', max_length=64, blank=False, null=False)
    invoice = models.OneToOneField(to=Invoice, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Payment'
        verbose_name_plural = 'Payments'

    def __str__(self):
        """Payment name."""
        return f'{self.payment_id} - {self.status}'
