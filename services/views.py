"""Services views."""
from rest_framework import viewsets

from .models import (
    Service,
    GradeRange,
    Homework,
    ServiceLevel,
    ServiceType,
)
from .serializers import (
    ServiceSerializer,
    HomeworkSerializer,
    GradeRangeSerializer,
    ServiceLevelSerializer,
    ServiceTypeSerializer,
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


class GradeRangeViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that serves grade ranges to be viewed only.
    """

    queryset = GradeRange.objects.all()
    serializer_class = GradeRangeSerializer


class ServiceLevelViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that serves service level to be viewed only.
    """

    queryset = ServiceLevel.objects.all()
    serializer_class = ServiceLevelSerializer


class ServiceTypeViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that serves service type to be viewed only.
    """

    queryset = ServiceType.objects.all()
    serializer_class = ServiceTypeSerializer
