from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe

from itrac.models import Comment, Issue
from .itrac_utils import send_email_update
from core.constants import ACTIVE_STATUS


# Send a notification when a comment is created or updated
@receiver(post_save, sender=Comment)
def notification_new_issue_comment(sender, instance, created, **kwargs):
    recipients = []
    watchers = instance.issue.watchers.all()
    
    if watchers.count():
        recipients = list(map(lambda w: w.watcher.email, watchers))
    else:
        return

    subject = f'''iTrac: { instance.issue.coded_id} {instance.issue.title}'''

    if created: 
            text_template = 'itrac/email_notification/message_comment_created.txt'
            html_template = 'itrac/email_notification/message_comment_created.html',
    else:
        if instance.active_status_cd == ACTIVE_STATUS.DELETED:
            text_template = 'itrac/email_notification/message_comment_deleted.txt'
            html_template = 'itrac/email_notification/message_comment_deleted.html',
        else:
            text_template = 'itrac/email_notification/message_comment_updated.txt'
            html_template = 'itrac/email_notification/message_comment_updated.html',

    text_message = render_to_string(
            'itrac/email_notification/message_comment_created.txt',
            { 'comment': instance }
        ) 
    html_message = render_to_string(
            'itrac/email_notification/message_comment_created.html',
            { 'comment': instance }
        ) 
    send_email_update(subject, text_message, recipients, html_message)


@receiver(pre_save, sender=Issue)
def notification_issue_changed(sender, instance, **kwargs):
    changes_txt = []
    changes_html = []
    try:
        issue = sender.objects.get(pk=instance.pk)
    except sender.DoesNotExist:
        # pass # Object is new, so field hasn't technically changed, but you may want to do something else here.
        return
    else:
        if issue.status != instance.status: # Field has changed
            changes_txt.append(f'Status was changed from { issue.get_status_display() } to { instance.get_status_display() }')        
            changes_html.append(mark_safe(f'''Status was changed from { issue.get_status_display() } to 
                        <b>{ instance.get_status_display() }</b>'''))        

        if issue.assignee != instance.assignee:
            changes_txt.append(f'Assignee was changed from { issue.assignee } to { instance.assignee }')        
            changes_html.append(mark_safe(f'Assignee was changed from { issue.assignee } to <b>{ instance.assignee }</b>'))        
        
        if issue.issue_type != instance.issue_type:
            changes_txt.append(f'Issue Type was changed from { issue.get_issue_type_display() } to { instance.get_issue_type_display() }')        
            changes_html.append(mark_safe(f'Issue Type was changed from { issue.get_issue_type_display() } to <b>{ instance.get_issue_type_display() }</b>'))        

        if issue.description != instance.description:
            changes_txt.append(f'Issue description was changed from { issue.get_description_as_markdown() } to { instance.get_description_as_markdown() }')        
            changes_html.append(mark_safe(f'Issue description was changed from { issue.get_description_as_markdown() } to <b>{ instance.get_description_as_markdown() }</b>'))        

    if len(changes_html):
        recipients = []
        watchers = issue.watchers.all()
        
        if watchers.count():
            recipients = list(map(lambda w: w.watcher.email, watchers))
        else:
            return

        subject = f'''iTrac: { issue.coded_id} { issue.title }'''
        text_message = render_to_string(
                'itrac/email_notification/message_issue_changed.txt',
                { 'issue': instance, 'changes': changes_txt }
            ) 
        html_message = render_to_string(
                'itrac/email_notification/message_issue_changed.html',
                { 'issue': instance, 'changes': changes_html }
            ) 
        send_email_update(subject, text_message, recipients, html_message)
