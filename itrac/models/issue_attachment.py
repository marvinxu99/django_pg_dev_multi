from django.db import models
from django.utils import timezone
from django.conf import settings
from django.utils.translation import gettext_lazy as _ 
from django.urls import reverse
from markdown import markdown
from django.utils.html import mark_safe

from .issue import Issue

class IssueAttachment(models.Model):
    """
    A single attachment
    """
    description = models.CharField(max_length=255, blank=True)
    attachment = models.FileField(upload_to=get_directory_path)
    issue = models.ForeignKey(Issue, related_name='att_issue', on_delete=models.CASCADE)

    uploaded_at = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='att_uploader', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "issue_attachment"
        verbose_name_plural = "issue_attachments"
        ordering = ['description']
        indexes = [
            models.Index(fields=['description']),
        ]

    def __str__(self):
        return self.description

    def get_directory_path(self):
        return f'itrac/{self.issue.project.code}/{self.issue.id}/'
