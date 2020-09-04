"""Users app models."""

from django.db import models


class Customer(models.Model):
    """Customer model."""

    email = models.EmailField('Email address', blank=False)

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

    def __str__(self):
        """Customer name."""
        return f'{self.email}'
