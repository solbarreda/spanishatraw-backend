from django.urls import include, path
from rest_framework import routers

from .views import (
    ServiceViewSet,
    GradeRangeViewSet,
    ServiceLevelViewSet,
    ServiceTypeViewSet,
    HomeworkViewSet,
    ServiceFilterValuesViewSet,
)

router = routers.DefaultRouter()
router.register(r'services', ServiceViewSet, basename='services')
router.register(r'grade-range', GradeRangeViewSet, basename='age-range')
router.register(
    r'service-level', ServiceLevelViewSet, basename='service-level')
router.register(r'service-type', ServiceTypeViewSet, basename='service-type')
router.register(r'homework', HomeworkViewSet, basename='homework')

urlpatterns = [
    path('', include(router.urls)),
    path(r'filter-options', ServiceFilterValuesViewSet.as_view(), name='filter-options')
]
