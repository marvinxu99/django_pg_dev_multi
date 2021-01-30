from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

# from .models import Issue
# from .views.itrac_utils import unique_slug_generator
from itrac.models import Issue, Comment
from .itrac_utils import send_email_update


# Send a notification when a comment is created or updated
@receiver(post_save, sender=Comment)
def notification_new_issue_comment(sender, instance, created, **kwargs):
    if created: 
        # instance.coded_id = f'{ instance.project.code }-{ instance.pk }'
        # instance.save()
        print('new comment created.')
        send_email_update("test", "comment created.", ['marvinxu99@hotmail.com',])
    else:
        print('comment updated.')
        send_email_update("test", "comment updated.", ['marvinxu99@hotmail.com',])
