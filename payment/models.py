from django.db import models
from django.contrib.auth import get_user_model


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

    service = models.OneToOneField(
        verbose_name='Invoice',
        to='services.Service',
        on_delete=models.DO_NOTHING)
    charged_amount = models.DecimalField(
        verbose_name='Charged amount', max_digits=8, decimal_places=2)
    timestamp = models.DateTimeField(
        verbose_name='Timestamp', auto_now_add=True, null=False)
    user = models.ForeignKey(
        verbose_name='User', to=get_user_model(), on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = 'Invoice'
        verbose_name_plural = 'Invoices'

    def __str__(self):
        """Invoice name."""
        return f'{self.user.email} - {self.service}'
