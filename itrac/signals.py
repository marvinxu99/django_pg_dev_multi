from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

# from .models import Issue
# from .views.itrac_utils import unique_slug_generator


# update the issue.coded_id
# @receiver(post_save, sender=Issue)
# def set_issue_coded_id(sender, instance, created, **kwargs):
#     if created: 
#         instance.coded_id = f'{ instance.project.code }-{ instance.pk }'
#         instance.save()

# # update the issue_prefix
# @receiver(pre_save, sender=Issue)
# def set_issue_slug(sender, instance, **kwargs):
#     if not instance.slug:
#         instance.slug = unique_slug_generator(instance)
