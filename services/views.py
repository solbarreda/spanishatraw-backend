from rest_framework import viewsets
from rest_framework import permissions

from .models import (
    Service,
    AgeRange,
    Homework,
)
from .serializers import (
    ServiceSerializer,
    HomeworkSerializer,
    AgeRangeSerializer,
)


class ServiceViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that serves services to be viewed only.
    """

    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class HomeworkViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that serves homeworks to be viewed only.
    """

    queryset = Homework.objects.all()
    serializer_class = HomeworkSerializer


class AgeRangeViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that serves age ranges to be viewed only.
    """

    queryset = AgeRange.objects.all()
    serializer_class = AgeRangeSerializer
