from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Issue


# update the issue_prefix
@receiver(post_save, sender=Issue)
def set_issue_prefix(sender, instance, **kwargs):
    # # print("post_save TransEvent.")
    # if not instance.event_id: 
    #     instance.event_id = instance.trans_event_id
    #     instance.save()
    pass
