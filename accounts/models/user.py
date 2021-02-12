from django.contrib.auth.models import AbstractUser
from django.db import models
from .person import Person
from .prsnl import Prsnl


class User(AbstractUser):
    user_id = models.BigAutoField(primary_key=True, editable=False)
    # first_name = None
    # last_name = None

    def get_full_name(self):
        try:
            if self.is_staff:
                p = Prsnl.objects.filter(user=self)[0]
            else:
                p = Person.objects.filter(user=self)[0]
            full_name = p.name_full_formatted
        except:
            full_name = "-"
        return full_name
    get_full_name.admin_order_field = 'name_last'
    get_full_name.short_description = 'full name'

    def get_name(self):
        try:
            if self.is_staff:
                p = Prsnl.objects.filter(user=self)[0]
            else:
                p = Person.objects.filter(user=self)[0]
            name = p.first_name + ' ' + p.last_name
        except:
            name = "-"
        return name
    get_name.admin_order_field = 'name'
    get_name.short_description = 'name'

    def __str__(self):
        return f'{ self.first_name } { self.last_name } ({ self.username })'
