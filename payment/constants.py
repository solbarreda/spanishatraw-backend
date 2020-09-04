"""Constants."""

PAYPAL = 'paypal'
PAYMENT_GATEWAYS = (
    (PAYPAL, 'paypal',),
)

PENDING_STATUS = 'pending'
COMPLETED_STATUS = 'completed'
PAYMENT_STATUS = (
    (PENDING_STATUS, 'pending',),
    (COMPLETED_STATUS, 'completed',),
)
