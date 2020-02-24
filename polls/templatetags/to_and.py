"""
Replacing a character in Django template
https://stackoverflow.com/questions/21483003/replacing-a-character-in-django-template

Custom template tags and filters
https://docs.djangoproject.com/en/dev/howto/custom-template-tags/#registering-custom-filters

For a ton of examples, read the source code for Django’s default filters and tags. 
They’re in django/template/defaultfilters.py and django/template/defaulttags.py, respectively.

"""

from django import template

register = template.Library()


@register.filter
def to_and(value):
    return value.replace("&", "and")


"""
In template , use:
    {% load to_and %}
then you can enjoy:
    {{ string|to_and }}
"""
