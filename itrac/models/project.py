from django.db import models
from django.urls import reverse
from django.conf import settings


class Project(models.Model):
    """
    A single project
    """   
    title = models.CharField(max_length=150)
    code = models.CharField(max_length=20, default="WINN")
    slug =  models.CharField(max_length=250)
    category = models.CharField(max_length=40, null=True)
    URL = models.CharField(max_length=250, null=True)

    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='project_created_by', on_delete=models.CASCADE)
    updated_date = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='project_updated_by', on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "project"
        verbose_name_plural = "projects"
        ordering = ['title']
        indexes = [
            models.Index(fields=['title',]),
        ]
