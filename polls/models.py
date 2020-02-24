import uuid
from django.db import models

import datetime
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return (now - datetime.timedelta(days=1)) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

    def was_published_today(self):
        return self.pub_date.date() == datetime.date.today()


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class Person(models.Model):
    person_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    name_first = models.CharField("Fist Name", max_length=128)
    name_middle = models.CharField("Middle Name", max_length=128, blank=True)
    name_last = models.CharField("Last Name", max_length=128)
    name_full_formatted = models.CharField("Full Name", max_length=128)
    is_active = models.BooleanField("Active")
    active_status_cd = models.IntegerField("Active Status")
    active_status_dttm = models.DateTimeField("Active Status Date")
    person_type_cd = models.IntegerField('User Type')
    created_dttm = models.DateTimeField("Date Created")
    update_dttm = models.DateTimeField("Date Updated")
    update_id = models.IntegerField("Updated by")

    def __str__(self):
        return self.name_full_formatted
