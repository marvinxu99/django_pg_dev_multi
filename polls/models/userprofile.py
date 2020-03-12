'''
https://stackoverflow.com/questions/44106679/custom-django-user-model-with-uuid-as-the-id-field?rq=1
To get the custom user model, subclass it form django.contrib.auth.models.AbstractUser 
and specify AUTH_USER_MODEL in your settings: AUTH_USER_MODEL = 'youruserapp.UserProfile'
'''
import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models

class UserProfile(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)

    