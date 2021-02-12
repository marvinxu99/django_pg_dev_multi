from django.core.mail import send_mail
from django.conf import settings
import string
from django.utils.text import slugify
import random


def random_string_generator(size = 10, chars = string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def unique_slug_generator(instance, new_slug = None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug = slug).exists()

    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
            slug = slug, randstr = random_string_generator(size = 4))

        return unique_slug_generator(instance, new_slug = new_slug)
    return slug


def send_email_update(subject, message, recipients, html_message):
    email_from = settings.EMAIL_HOST_USER
    send_mail(subject, message, email_from, recipients, html_message=html_message)
    return
