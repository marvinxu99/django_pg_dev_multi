from django.db import models
from django.urls import reverse
from django.conf import settings

from core.models import CodeValue 
from core.constants import CODE_SET


class Product(models.Model):
    # Use code set: 2 - Product Category
    category_cd = models.ForeignKey(CodeValue, 
                                related_name='products',     # '+': Do not create backwards relation to this model 
                                on_delete=models.CASCADE,
                                limit_choices_to={'code_set': CODE_SET.PRODUCT_CATEGORY, 'active_ind': 1},
                                verbose_name="Category"
                            )
    
    slug = models.SlugField(max_length=100, db_index=True)
    display = display = models.CharField(max_length=100)
    name = models.CharField(max_length=100, db_index=True)
    description = models.CharField(max_length=250)

    active_ind = models.BooleanField("Active", default=True)

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
        indexes = [
            models.Index(fields=['name'], name='p_name_idx'),
            models.Index(fields=['display'], name='p_display_idx'),
        ]
        permissions = (
            ("can_load_shop_data", "can load shop data"),
        )


    def __str__(self):
        return self.display

    def product_img_url(self):
        return f'{ settings.MEDIA_URL }{ self.image }'

    # def get_absolute_url(self):
    #     return reverse('shop:product_detail', args=[self.id, self.slug])
