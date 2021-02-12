from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver


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
    link_from_type = models.CharField(max_length=2, choices=ISSUE_LINK_TYPE.choices, default=ISSUE_LINK_TYPE.RELATES_TO)
    linked_to_issue = models.ForeignKey('Issue', related_name='linked_from_issues', on_delete=models.CASCADE)
    link_to_type = models.CharField(max_length=2, choices=ISSUE_LINK_TYPE.choices, default=ISSUE_LINK_TYPE.RELATES_TO)

    updated_date = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='+', on_delete=models.CASCADE, blank=True)

    class Meta:
        db_table = "itrac_issue_issue_link"

    def __str__(self):
        return f'{ self.linked_from_issue } linked to { self.linked_to_issue }'

# For setting link_to_type post_save
LINK_TO_TYPE_MAP = {
    '01': '01',
    '02': '03',
    '03': '02',
    '04': '05',
    '05': '04',
    '06': '07',
    '07': '06',
    '08': '09',
    '09': '08',
}

# update
@receiver(post_save, sender=IssueToIssueLink)
def set_issue_link_to_type(sender, instance, created, **kwargs):
    if created:
        instance.link_to_type = LINK_TO_TYPE_MAP[instance.link_from_type]
        instance.save()
