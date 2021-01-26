from django import template
from itrac.models import Issue

register = template.Library()


@register.simple_tag
def is_watcher(user, issue):
    for w in issue.watchers.all():
        if w.watcher == user:
            return True
    return False
