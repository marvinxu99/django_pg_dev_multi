from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.html import mark_safe
from django.utils.translation import gettext_lazy as _
from markdown import markdown

from core.constants import ACTIVE_STATUS
from .issue import Issue


class Comment(models.Model):
    """
    A single Comment
    """
    active_ind = models.BooleanField("Active", default=True)
    active_status_cd = models.CharField(max_length=2,
                                        choices=ACTIVE_STATUS.choices,
                                        default=ACTIVE_STATUS.ACTIVE
                                    )
    active_status_dt_tm = models.DateTimeField(null=True, blank=True)
    active_status_prsnl_id = models.BigIntegerField(default=0, blank=True)
    comment = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    updt_cnt = models.IntegerField(default=0)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='comment_author', on_delete=models.CASCADE)
    issue = models.ForeignKey(Issue, related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.comment

    def get_comment_as_markdown(self):
        return mark_safe(markdown(self.comment, safe_mode='escape'))
