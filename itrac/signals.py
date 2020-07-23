from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from .models import Issue
from .views.itrac_utils import unique_slug_generator

# update the issue_prefix
# @receiver(post_save, sender=Issue)
# def set_issue_prefix(sender, instance, **kwargs):
#     # print("post_save TransEvent.")
#     # if not instance.event_id: 
#     #     instance.event_id = instance.trans_event_id
#     #     instance.save()
#     pass

# update the issue_prefix
@receiver(pre_save, sender=Issue)
def set_issue_slug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
