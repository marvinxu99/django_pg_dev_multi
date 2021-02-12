from django.db import models
from django.conf import settings


# Shopping Care
class Cart(models.Model):
    """ Shopping cart
    """
    cart_id = models.BigAutoField(primary_key=True, editable=False)
    active_ind = models.BooleanField("Active", default=True)

    description = models.CharField(max_length=200, blank=True, null=True)

    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                            related_name='cart',
                            on_delete=models.SET_NULL,
                            null=True, blank=True)

    comment =  models.CharField(max_length=255, blank=True)

    create_dt_tm = models.DateTimeField(auto_now_add=True)
    create_id = models.BigIntegerField(default=0)
    updt_cnt = models.IntegerField(default=0)
    updt_dt_tm = models.DateTimeField(auto_now=True)
    updt_id = models.BigIntegerField(default=0)

    class Meta:
        db_table = 'shop_cart'

    def __str__(self):
        """String for representing the Model object."""
        return f"{ self.owner }'s { self.description.lower() }"
