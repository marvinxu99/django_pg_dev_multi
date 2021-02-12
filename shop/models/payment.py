from django.db import models

from shop.models import Order


class Payment(models.Model):
    """ Stores items in shopping care
    ."""
    payment_id = models.BigAutoField(primary_key=True, editable=False)

    description = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=False)

    comment =  models.CharField(max_length=255, blank=True)

    order = models.ForeignKey(Order, related_name='payments', on_delete=models.CASCADE)

    create_dt_tm = models.DateTimeField(auto_now_add=True)
    create_id = models.BigIntegerField(default=0)
    updt_cnt = models.IntegerField(default=0)
    updt_dt_tm = models.DateTimeField(auto_now=True)
    updt_id = models.BigIntegerField(default=0)

    class Meta:
        indexes = [
            models.Index(fields=['description',]),
        ]
        db_table = 'shop_payment'
        ordering = ('-create_dt_tm', )


    def __str__(self):
        """String for representing the Model object."""
        return f'{self.description}, ${self.amount}'
