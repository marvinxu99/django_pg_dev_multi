from django.conf import settings
from django.db import models

from .issue import Issue


class IssueWatcher(models.Model):
    """
    Watcher
    """
    watcher = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='+', on_delete=models.CASCADE)
    issue = models.ForeignKey(Issue, related_name='watchers', on_delete=models.CASCADE)

    class Meta:
        db_table = "itrac_issue_watcher"
        verbose_name = "issue_watcher"
        verbose_name_plural = "issue_watchers"
        ordering = ['watcher']

    def __str__(self):
        return f'{self.issue}: {self.watcher}'

    @property
    def full_name(self):
        return f'{ self.watcher.first_name } { self.watcher.last_name }'
