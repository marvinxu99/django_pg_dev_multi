from django.db import models
from django.utils import timezone
from django.conf import settings
from django.utils.translation import gettext_lazy as _ 
from django.urls import reverse
from markdown import markdown
from django.utils.html import mark_safe

from itrac.models import Issue, Comment



class CommentHistory(models.Model):
    """
    Comment History (only stores history of changes. 
    (if a row is delete, it is should still be in Comment table marked a "deleted")
    """
    parent_comment = models.ForeignKey(Comment, related_name='comment_hist', on_delete=models.CASCADE) 
    comment = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='+', on_delete=models.CASCADE)
    issue = models.ForeignKey(Issue, related_name='+', on_delete=models.CASCADE)
    updt_cnt = models.IntegerField(default=0)
    updt_dt_tm = models.IntegerField(default=0)

    class Meta:
        db_table = "itrac_comment_hist"
        verbose_name = "comment_history"
        verbose_name_plural = "comment_history"
        ordering = ['-updt_dt_tm']


    def __str__(self):
        return self.comment

    def get_comment_as_markdown(self):
        return mark_safe(markdown(self.comment, safe_mode='escape'))
