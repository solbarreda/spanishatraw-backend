from django.db import models


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

    def __str__(self):
        """Price name."""
        return f'{self.currency} {self.amount}'
