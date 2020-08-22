"""Services views."""
from rest_framework import viewsets, views
from rest_framework.response import Response
from django_filters import rest_framework as filters

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
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('type', 'level', 'grade_range')


class HomeworkViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that serves homeworks to be viewed only.
    """

    queryset = Homework.objects.all()
    serializer_class = HomeworkSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = (
        'service__type', 'service__level', 'service__grade_range', 'service')


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


class ServiceFilterValuesViewSet(views.APIView):
    """View to get service filter options based on level, range and type."""

    def get(self, request, format=None):
        """Return a list of all options."""
        response = {
            'levels': ServiceLevel.objects.all().values('id', 'description'),
            'grades': GradeRange.objects.all().values(
                'id', 'min', 'max'),
            'types': ServiceType.objects.all().values('id', 'description'),
            'services': Service.objects.all().values('id', 'name'),
        }
        return Response(response)
