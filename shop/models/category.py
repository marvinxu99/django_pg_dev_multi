from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True)

    active_ind = models.BooleanField("Active", default=True)
    
    create_dt_tm = models.DateTimeField(auto_now_add=True)
    create_id = models.BigIntegerField(default=0)
    updt_cnt = models.IntegerField(default=0)
    updt_dt_tm = models.DateTimeField(auto_now=True)  
    updt_id = models.BigIntegerField(default=0)

    class Meta:
        ordering = ('name', )
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        indexes = [
            models.Index(fields=['name',]),
            models.Index(fields=['slug',]),
        ]
        db_table = 'shop_category'

    def __str__(self):
        return self.name

#    def get_absolute_url(self):
#        return reverse('shop:product_list_by_category', args=[self.slug])

