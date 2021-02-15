from django.conf import settings
from django.db import models
from django.urls import reverse


def get_avatar_full_path(instance, filename):
    ext = filename.split('.')[-1]
    path = f'{settings.MEDIA_PUBLIC_ROOT}/project/avatars'
    name = f'{instance.pk}_{instance.avatar_version:04d}'
    return f'{path}/{name}.{ext}'


class Project(models.Model):
    """
    A single project
    """
    title = models.CharField(max_length=100)
    code = models.CharField(max_length=20, default="WINN")
    description = models.CharField(max_length=250, null=True, blank=True)
    slug =  models.CharField(max_length=250)
    category = models.CharField(max_length=40, null=True, blank=True)
    URL = models.CharField(max_length=250, null=True, blank=True)

    is_active = models.BooleanField(default=True)

    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='project_created_by', on_delete=models.CASCADE)
    updated_date = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='project_updated_by', on_delete=models.CASCADE, blank=True)

    avatar = models.ImageField(upload_to=get_avatar_full_path, blank=True)
    avatar_version = models.IntegerField(default=0, blank=True, editable=False)

    class Meta:
        verbose_name = "project"
        verbose_name_plural = "projects"
        ordering = ['title']
        indexes = [
            models.Index(fields=['title']),
        ]

    def __str__(self):
        return self.title

    @property
    def get_issues_count(self):
        return self.issues.count()

    @property
    def get_issues_count_unresolved(self):
        return self.issues.filter(is_resolved=False).count()
