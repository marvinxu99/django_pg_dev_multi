from django.db import models
from django.urls import reverse
from django.conf import settings


class Tag(models.Model):
    """
    A single tag
    """
    title = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)

    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='tags', on_delete=models.CASCADE)
    updated_date = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "tag"
        verbose_name_plural = "tags"
        ordering = ['title']
        indexes = [
            models.Index(fields=['title',]),
        ]

    def get_issues_count(self):
        return self.issues.count()
