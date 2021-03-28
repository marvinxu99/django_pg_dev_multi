from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe

from accounts.models import User

from core.core_utils import send_email_update


# Send a notification when a user is created or updated
@receiver(post_save, sender=User)
def notification_new_user_created(sender, instance, created, **kwargs):

    recipients = []
    recipients.append("winnpysoft@gmail.com")

    subject = f'''Account: New user created or updated.'''

    if created:
        text_template = 'accounts/email_notification/message_user_created.txt'
        html_template = 'accounts/email_notification/message_user_created.html',

        text_message = render_to_string(
                text_template,
                {'user': instance}
            )
        html_message = render_to_string(
                html_template,
                {'user': instance}
            )
        send_email_update(subject, text_message, recipients, html_message)


# @receiver(pre_save, sender=User)
# def notification_user_changed(sender, instance, **kwargs):
#     pass
