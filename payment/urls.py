from django.urls import include, path
from rest_framework import routers

from .views import (
    InvoiceViewSet,
)

router = routers.DefaultRouter()
router.register(r'invoice', InvoiceViewSet, basename='invoice')

urlpatterns = [
    path('', include(router.urls)),
]
