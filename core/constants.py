from django.db import models
import calendar
from django.utils.translation import gettext_lazy as _



class ACTIVE_STATUS(models.TextChoices):
    ACTIVE = '01', _("Active")
    COMBINED = '02', _('Combined') 
    COMBINEHIST = '03', _('Historical value - combined')
    DELETED = '04', _('Deleted')
    DRAFT = '05', _('Draft')
    INACTIVE = '06', _('Inactive')
    RECALL = '07', _('Recall')
    REVIEW = '08', _('Review')
    SUSPENDED = '09', _('Suspended')
    UNKNOWN = '10', _('Unknown')

# Unit of Measure(UOM) - all
class UOM(models.TextChoices):
    DEGC = 'C', _("degree Celsius")
    DEGC = 'F', _("degree Fahrenheit")

# Unit of Measure(UOM) - temperature
class UOM_TEMP(models.TextChoices):
    DEGC = 'C', _("degree Celsius")
    DEGC = 'F', _("degree Fahrenheit")

# Loan Status
class LOAN_STATUS(models.TextChoices):
    AVAILABLE = 'a', _('Available')
    MAINTENANCE = 'm', _('Maintenance')
    ON_LOAN = 'o', _('On loan')
    RESERVED = 'r', _('Reserved')


#MONTH_CHOICES = [(str(i), calendar.month_name[i]) for i in range(1,13)]
class MONTH_CHOICES(models.TextChoices):
    JAN = '1', _("January")
    FEB = '2', _("Febuary")
    MAR = '3', _("March")
    APR = '4', _('April')
    MAY = '5', _('May')
    JUN = '6', _('June')
    JUL = '7', _('July')
    AUG = '8', _('August')
    SEP = '9', _('September')
    OCT = '10', _('October')
    NOV = '11', _('November')
    DEC = '12', _('December')


MEDIA_CHOICES = [
    ('Audio', (
            ('vinyl', 'Vinyl'),
            ('cd', 'CD'),
        )
    ),
    ('Video', (
            ('vhs', 'VHS Tape'),
            ('dvd', 'DVD'),
        )
    ),
    ('unknown', 'Unknown'),
]


