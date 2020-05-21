from django.db import models
from django.utils import timezone
from .utils import ChoiceEnum
from django.conf import settings

class Issue(models.Model):
    """
    A single Issue
    """
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_resolved = models.BooleanField(default=False)
    resolved_date = models.DateTimeField(blank=True, null=True)
    upvotes = models.IntegerField(default=0)
    tag = models.CharField(max_length=30, blank=True, null=True)
    image = models.ImageField(upload_to='img', blank=True, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='issue_author', on_delete=models.CASCADE)
    assignee = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='issue_assignee', null=True, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    # Encapsulation, we meet again.
    class Issue_Types(ChoiceEnum):
        BREAK_FIX = 'Break/fix'
        FEATURE = 'New feature'
        OPTIMIZATION ='Optimization'

    class Statuses(ChoiceEnum):
        OPEN = 'Open'
        INVESTIGATE = 'Investigate'
        TRRIAGE ="Await Approval"
        BUILD_IN_PROGRESS = 'Build in progress'
        VALIDATE = 'Validate'
        COMPLETE = 'Complete'
        CLOSED = 'Closed'

    issue_type = models.CharField(max_length=20, choices=Issue_Types.choices(), default='BREAK_FIX')
    status = models.CharField(max_length=20, choices=Statuses.choices(), default='TODO')


    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title


class Comment(models.Model):
        """
        A single Comment
        """
        comment = models.CharField(max_length=200)
        created_date = models.DateTimeField(auto_now_add=True)
        updated_date = models.DateTimeField(auto_now=True)
        author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='comment_author', on_delete=models.CASCADE)
        issue = models.ForeignKey(Issue, related_name='comment_issue', on_delete=models.CASCADE)

        def __unicode__(self):
            return self.comment

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


