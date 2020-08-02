from django.db import models
from django.utils import timezone
from django.conf import settings
from django.utils.translation import gettext_lazy as _ 
from django.urls import reverse
from markdown import markdown
from django.utils.html import mark_safe

from .issue import Issue

class Comment(models.Model):
    """
    A single Comment
    """
    comment = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='comment_author', on_delete=models.CASCADE)
    issue = models.ForeignKey(Issue, related_name='comment_issue', on_delete=models.CASCADE)

    def __str__(self):
        return self.comment

    def get_comment_as_markdown(self):
        return mark_safe(markdown(self.comment, safe_mode='escape'))
