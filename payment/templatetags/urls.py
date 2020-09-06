"""Django Url template tags."""

from django import template
from django.contrib.sites.models import Site

register = template.Library()


@register.simple_tag
def full_url():
    """Retrieve site url."""
    return Site.objects.all().first().domain
