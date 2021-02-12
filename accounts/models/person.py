# import uuid
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.utils import timezone


class Person(models.Model):
    # person_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    person_id = models.BigAutoField(primary_key=True, editable=False)

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        limit_choices_to={'is_staff': False},
        verbose_name='username',
        help_text='Each person must have a username which is used to login to the system',
    )

    name_first = models.CharField("Fist Name", max_length=128, default='John')
    name_middle = models.CharField("Middle Name", max_length=128, blank=True, null=True)
    name_last = models.CharField("Last Name", max_length=128, default='Doe')
    name_full_formatted = models.CharField("Full Name", max_length=128, default='John Doe, MD')
    is_active = models.BooleanField("Active", default=True)
    active_status_cd = models.IntegerField("Active Status", default=1)
    active_status_dt_tm = models.DateTimeField("Active Status Date", auto_now_add=True)
    person_type_cd = models.IntegerField('User Type', default=1)

    created_dt_tm = models.DateTimeField("Date Created", null=True, blank=True)
    create_id = models.BigIntegerField('Created by', null=True, blank=True)

    updated_dt_tm = models.DateTimeField("Date Updated", null=True, blank=True)
    update_id = models.BigIntegerField('Updated by', null=True, blank=True)

    class Meta:
        ordering = ['name_last']
        verbose_name = 'Person'
        #verbose_name_plural = "Customers"

    def __str__(self):
        return self.name_full_formatted


@receiver(post_save, sender=User)
def create_user_person(sender, instance, created, **kwargs):
    if created:
        instance.created_dt_tm = timezone.now()
        instance.person.create_id = instance.user.user_id
        Person.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_person(sender, instance, **kwargs):
    instance.person.updated_dt_tm = timezone.now()
    instance.person.update_id = instance.user.user_id
    instance.person.save()


class Person_Alias(models.Model):
    # person_alias_id = models.UUIDField(
    #     primary_key=True, default=uuid.uuid4, editable=False)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    person_alias_id = models.BigAutoField(primary_key=True, editable=False)

    is_active = models.BooleanField('Active', default=True)
    active_status_cd = models.IntegerField('Ative Status', default=1)
    alias = models.CharField('Alias', max_length=200, default='abc')
    alias_expiry_dt_tm = models.DateTimeField("Alias Expiry Date", null=True, blank=True)
    alias_pool_cd = models.IntegerField('Alias Type', default=1)

    def __str__(self):
        return self.alias
