from django.db import models
from django.utils import timezone
from django.conf import settings
from django.utils.translation import gettext_lazy as _ 
from django.urls import reverse

from .tag import Tag

#from django.apps import apps
#MyModel1 = apps.get_model('app1', 'MyModel1')

class ISSUE_TYPE(models.TextChoices):
    BREAK_FIX =     '01', _('Break/fix')
    FEATURE =       '02', _('New feature')
    OPTIMIZATION =  '03', _('Optimization')


class ISSUE_STATUS(models.TextChoices):
    OPEN =          '01', _('Open')
    INVESTIGATE =   '02', _('Investigate')
    TRIAGE =        '03', _('Await approval')
    BUILD_IN_PROGRESS = '04', _('Build in progress')
    VALIDATING =    '05', _('Validate in progress')
    COMPLETE =      '06', _('Complete')
    CLOSED =        '07', _('Closed')


class Issue(models.Model):
    """
    A single Issue
    """
    # The prefix is specfic to a project or subproject
    issue_prefix = models.CharField(max_length=20, default='WINN')
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    slug = models.CharField(max_length=250, blank=True)
    
    is_resolved = models.BooleanField(default=False)
    resolved_date = models.DateTimeField(blank=True, null=True)
    upvotes = models.IntegerField('likes', default=0)
    
    tags = models.ManyToManyField(Tag, related_name='issues', blank=True)
    
    image = models.ImageField(upload_to='img', blank=True, null=True)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='issue_author', on_delete=models.CASCADE)
    assignee = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='issue_assignee', null=True, on_delete=models.CASCADE)

    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    issue_type = models.CharField(max_length=2, choices=ISSUE_TYPE.choices, default=ISSUE_TYPE.BREAK_FIX)
    status = models.CharField(max_length=2, choices=ISSUE_STATUS.choices, default=ISSUE_STATUS.OPEN)

    class Meta:
        verbose_name = "issue"
        verbose_name_plural = "issues"
        ordering = ['title']
        indexes = [
            models.Index(fields=['title',]),
        ]

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    @property
    def issue_id(self):
        return f"{self.issue_prefix}-{self.id}"

    def get_absolute_url(self):
        return reverse('itrac:issue_detail', args=(self.slug,))


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


class Reply(models.Model):
    """
    A single reply
    """
    reply = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='reply_author', on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, related_name='reply_comment', on_delete=models.CASCADE)

    def __unicode__(self):
        return self.reply

    def __str__(self):
        return self.reply


class SavedIssue(models.Model):
    """
    A single SavedIssue
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_savedissue', on_delete=models.CASCADE)
    issue = models.ForeignKey(Issue, related_name='issue_savedissue', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)


