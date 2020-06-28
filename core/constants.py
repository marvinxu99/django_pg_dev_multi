from django.db import models
import calendar
from django.utils.translation import gettext_lazy as _ 

#from django.apps import apps
#MyModel1 = apps.get_model('app1', 'MyModel1')

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

class ENTRY_MODE(models.TextChoices):
    SCAN_N_PAY = '01', _("Scan-N-Pay")
    ESI = '02', _('ESI') 
    DIRECT_ENTRY = '03', _('Direct Entry')
    CASHIER = '04', _('Cashier')

# Item Types
class ITEM_TYPE(models.TextChoices):
    GENERAL = '12', _('General')
    PRODUCE = '13', _('Produce')
    DAIRY = '14', _('Dairy')
    ITEM_EQP = '03', _('Equipment Master')
    ITEM_GROUP = '04', _('Equipment Group')
    ITEM_MANF = '05', _('Manufacturer Item')
    ITEM_MASTER = '06', _('Item Master')
    ITEM_VENDOR = '07', _('Vendor Item')
    LOT_INFO = '08', _('Lot Info')
    MED_DEF = '09', _('Medication')
    PO = '10', _('Purchase Order')
    REQUSITION = '11', _('Requisition')
    INSTANCE = '01', _('Instance')
    INSTANCE_EQP = '02', _('Equipment Instance')


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

# Media Choices - not used
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


# Price Type
class ITEM_PRICE_TYPE(models.TextChoices):
    CONTRACT = '01', _('Contract')		
    LIST = '02', _('List')
    QUOTE = '03', _('Quote')


# Product Identifier Type (excluding barcodes)
class ITEM_IDENTIFIER_TYPE(models.TextChoices):
    BRAND_NAME = '01', _('Brand Name')
    DESCRIPTION = '02', _('Description')
    DESC_CLINIC = '03',	_('Clinical Description')
    DESC_SHORT = '04', _('Short Description')
    FOREIGNALIAS ='05', _('Foreign System Item Alias')
    GENERIC_NAME = '06', _('Generic Name')
    TRADE_NAME = '07', _('Trade Name')

# Item barcodes (one item can have multiple barcodes)
class ITEM_BARCODE_TYPE(models.TextChoices):
    BARCODE = '20', _('Barcode')		
    CHARGE_NBR = '21', _('Charge Number')
    ITEM_NBR_SYS = '22', _('System Assigned Item Number')
    LOT_NBR	= '23', _('Lot Number')
    MANF_ITM_NBR ='24', _('Manufacturer Item Number')
    SERIAL_NBR = '25', _('Serial Number')
    SERVIC_REQ_NBR = '26', _('Service Request Number')
    UB92 = '27', _('UB92 Interface Identifier')
    UPC	= '28', _('Universal Product Code')
    UPN = '29', _('Universal Product Number')
    VENDOR_ITEM_NBR = '30', _('Vendor Item Number')

class TRANSACTION_TYPE(models.TextChoices):
    PURCHASE = '01', _('Purchase')		
    REFUND = '02', _('Refund')
    EXCHANGE = '03', _('Exchange')

class TRANS_COMMENT_TYPE(models.TextChoices):
    COMMENT_STAFF = '01', _('Staff Comment')		
    COMMENT_CLIENT = '02', _('Client Comment')
    COMMENT_AUDIT = '03', _('Audit Comment')
    COMMENT_SYSTEM = '04', _('System Comment')
    COMMENT_VOID = '05', _('Void Reason')


# Unit of Measure(UOM) - all
class UOM(models.TextChoices):
    DEGC = 'C', _("degree Celsius")
    DEGF = 'F', _("degree Fahrenheit")


# Unit of Measure(UOM) - shelf life
class UOM_SHELF_LIFE(models.TextChoices):
    HOURS = 'H', _("hours")
    DAYS = 'D', _("days")
    YEARS = 'Y', _("years")

# Unit of Measure(UOM) - temperature
class UOM_TEMP(models.TextChoices):
    DEGC = 'C', _("degree Celsius")
    DEGF = 'F', _("degree Fahrenheit")

