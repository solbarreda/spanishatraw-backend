from django.urls import include, path
from rest_framework import routers

from .views import (
    ServiceViewSet,
    AgeRangeViewSet,
    HomeworkViewSet,
)

router = routers.DefaultRouter()
router.register(r'services', ServiceViewSet, basename='services')
router.register(r'age-range', AgeRangeViewSet, basename='age-range')
router.register(r'homework', HomeworkViewSet, basename='homework')

urlpatterns = [
    path('', include(router.urls)),
]
