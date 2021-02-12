from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import TransEvent


# update the EVENT_ID to be the trans_event_id when the row is firs created
@receiver(post_save, sender=TransEvent)
def set_event_id(sender, instance, **kwargs):
    # # print("post_save TransEvent.")
    # if not instance.event_id:
    #     instance.event_id = instance.trans_event_id
    #     instance.save()
    pass
