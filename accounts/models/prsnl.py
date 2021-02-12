from django.db import models
from django.conf import settings
from django.db.models.functions import Concat
from django.db.models import Value
from django.utils.html import format_html


class Prsnl(models.Model):
    prsnl_id = models.BigAutoField(primary_key=True, editable=False)

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        limit_choices_to={'is_staff': True},
        verbose_name='username',
        help_text='Each staff member must have a username which is used to login to the Winter Winn system',
    )

    is_active = models.BooleanField('Active', default=True)
    active_status_cd = models.IntegerField('Ative Status', default=1)

    name_first = models.CharField("Fist Name", max_length=128, blank=True)
    name_middle = models.CharField("Middle Name", max_length=128, blank=True)
    name_last = models.CharField("Last Name", max_length=128, blank=True)
    name_full_formatted = models.CharField("Full Name", max_length=128, blank=True)

    COLOUR_CD = (
        ('red', 'Red'),
        ('blue', 'Blue'),
        ('orange', 'Orange'),
        ('green', 'Green'),
    )
    colour_code = models.CharField(
        max_length=6, choices=COLOUR_CD, default='green',
        help_text="The colour of their care team(not their skin colour)"
    )

    POSITION_CD = (
        ('P01', 'Physician - General Medicine'),
        ('P02', 'Physician - Critical Care'),
        ('P03', 'Physician - Emergency'),
        ('N01', 'Nurse'),
        ('N02', 'Nurse - ICU'),
        ('N03', 'Nurse - Emergency'),
        ('N04', 'Nurse - Ambulatory'),
        ('CEO', 'Chief Executive Officer'),
        ('CFO', 'Chief Financial Officer'),
        ('COO', 'Chief Operating Officer'),
        ('M01', 'General Manager'),
    )
    position = models.CharField(max_length=3, choices=POSITION_CD, default='N01')

    class Meta:
        verbose_name = "Personnel"
        verbose_name_plural = "Personnel"

    def __str__(self):
        return self.name_full_formatted

    def coloured_name(self):
        return format_html(
            '<span style="color: #{};">{} {}</span>',
            self.colour_code,
            self.name_first,
            self.name_last,
        )
    # coloured_name.admin_order_field = 'name_last'
    coloured_name.admin_order_field = Concat('name_first', Value(' '), 'name_last')


class Prsnl_Alias(models.Model):
    prsnl_alias_id = models.BigAutoField(primary_key=True, editable=False)
    prsnl = models.ForeignKey(Prsnl, on_delete=models.CASCADE)

    is_active = models.BooleanField('Active', default=1)
    active_status_cd = models.IntegerField('Ative Status', default=1)
    alias = models.CharField('Alias', max_length=200, default='abc')
    alias_expiry_dt_tm = models.DateTimeField("Alias Expiry Date", null=True, blank=True)
    alias_pool_cd = models.IntegerField('Alias Type', default=1)

    def __str__(self):
        return self.alias
