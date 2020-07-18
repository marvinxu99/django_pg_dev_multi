from django.db import models
from django.urls import reverse

class Tag(models.Model):
    """
    A single tag
    """   
    title = models.CharField(max_length=100)
    slug =  models.CharField(max_length=250)
    created_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "tag"
        verbose_name_plural = "tags"
        ordering = ['title']
        indexes = [
            models.Index(fields=['title',]),
        ]
