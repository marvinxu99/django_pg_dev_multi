from django.db import models
from django.conf import settings

from .issue import Issue


class SavedIssue(models.Model):
    """
    A single SavedIssue (Favourite Issue)
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_savedissues', on_delete=models.CASCADE)
    issue = models.ForeignKey(Issue, related_name='issue_savedissue', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
