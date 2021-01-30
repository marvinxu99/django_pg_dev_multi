from django import template
from django.conf import settings

register = template.Library()


@register.simple_tag
def get_domain_url():
    return settings.DOMAIN_URL

