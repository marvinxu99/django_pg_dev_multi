from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe

from itrac.models import Comment, Issue
from .itrac_utils import send_email_update


# Send a notification when a comment is created or updated
@receiver(post_save, sender=Comment)
def notification_new_issue_comment(sender, instance, created, **kwargs):
    recipients = []
    watchers = instance.issue.watchers.all()
    
    if watchers.count():
        recipients = list(map(lambda w: w.watcher.email, watchers))
    else:
        return

    if created: 
        # instance.coded_id = f'{ instance.project.code }-{ instance.pk }'
        # instance.save()
        subject = f'iTrac: { instance.issue.coded_id} {instance.issue.title}'
        text_message = render_to_string(
                'itrac/email_notification/message_comment_created.txt',
                { 'comment': instance }
            ) 
        html_message = render_to_string(
                'itrac/email_notification/message_comment_created.html',
                { 'comment': instance }
            ) 
        send_email_update(subject, text_message, recipients, html_message)
    else:
        subject = f'''iTrac: { instance.issue.coded_id} {instance.issue.title}'''
        text_message = (render_to_string(
                'itrac/email_notification/message_comment_created.txt',
                { 'comment': instance }
            )) 
        html_message = (render_to_string(
                'itrac/email_notification/message_comment_created.html',
                { 'comment': instance }
            )) 
        send_email_update(subject, text_message, recipients, html_message)


@receiver(pre_save, sender=Issue)
def notification_if_issue_changed(sender, instance, **kwargs):
    try:
        obj = sender.objects.get(pk=instance.pk)
    except sender.DoesNotExist:
        pass # Object is new, so field hasn't technically changed, but you may want to do something else here.
    else:
        if not obj.some_field == instance.some_field: # Field has changed
            pass # do something