import uuid
from django.db import models


class Person(models.Model):
    # person_id = models.UUIDField(
    #     primary_key=True, default=uuid.uuid4, editable=False)
    person_id = models.BigAutoField(primary_key=True, editable=False)

    name_first = models.CharField("Fist Name", max_length=128)
    name_middle = models.CharField("Middle Name", max_length=128, blank=True)
    name_last = models.CharField("Last Name", max_length=128)
    name_full_formatted = models.CharField("Full Name", max_length=128)
    is_active = models.BooleanField("Active")
    active_status_cd = models.IntegerField("Active Status")
    active_status_dt_tm = models.DateTimeField("Active Status Date")
    person_type_cd = models.IntegerField('User Type')
    created_dt_tm = models.DateTimeField("Date Created")
    update_dt_tm = models.DateTimeField("Date Updated")
    update_id = models.IntegerField("Updated by")

    def __str__(self):
        return self.name_full_formatted


# def pk_uuid4_hex():
#     return uuid.uuid4().int[:8]


class Person_Alias(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    # person_alias_id = models.UUIDField(
    #     primary_key=True, default=uuid.uuid4, editable=False)
    person_alias_id = models.BigAutoField(primary_key=True, editable=False)

    active_ind = models.BooleanField('Active')
    active_status_cd = models.IntegerField('Ative Status')
    alias = models.CharField('Alias', max_length=200)
    alias_expiry_dt_tm = models.DateTimeField("Alias Expiry Date")
    alias_pool_cd = models.BigIntegerField()
