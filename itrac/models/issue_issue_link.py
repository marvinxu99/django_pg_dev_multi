from django.db import models
from django.utils.translation import gettext_lazy as _ 
from django.conf import settings


class ISSUE_LINK_TYPE(models.TextChoices):
    RELATES_TO          = '01', _('relates to')
    BLOCKS              = '02', _('blocks')
    IS_BLOCKED_BY       = '03', _('is blocked by')
    CAUSES              = '04', _('causes')
    IS_CAUSED_BY        = '05', _('is caused by')
    CLONES              = '06', _('clones')
    IS_CLONED_BY        = '07', _('is cloned by')
    DUPLICATES          = '08', _('duplicates')
    IS_DUPLICATED_BY    = '09', _('is duplicated by')


class IssueToIssueLink(models.Model):
    linked_from_issue = models.ForeignKey('Issue', related_name='linked_to_issues', on_delete=models.CASCADE)
    link_type_from = models.CharField(max_length=2, choices=ISSUE_LINK_TYPE.choices, default=ISSUE_LINK_TYPE.RELATES_TO)
    linked_to_issue = models.ForeignKey('Issue', related_name='linked_from_issues', on_delete=models.CASCADE)
    link_type_to = models.CharField(max_length=2, choices=ISSUE_LINK_TYPE.choices, default=ISSUE_LINK_TYPE.RELATES_TO)
    
    updated_date = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='+', on_delete=models.CASCADE, blank=True)
    
    def __str__(self):
        return f'{ self.linked_from_issue } linked to { self.linked_to_issue }'

    class Meta:
        db_table = "itrac_issue_issue_link"
    