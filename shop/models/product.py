from django.db import models
from django.urls import reverse

from .core.models. 

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    stock = models.PositiveIntegerField()
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)

    create_dt_tm = models.DateTimeField(auto_now_add=True)
    create_id = models.BigIntegerField(default=0)
    updt_cnt = models.IntegerField(default=0)
    updt_dt_tm = models.DateTimeField(auto_now=True)  
    updt_id = models.BigIntegerField(default=0)

    class Meta:
        ordering = ('name', )
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])
