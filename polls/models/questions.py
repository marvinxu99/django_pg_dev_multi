import uuid
from django.db import models
from django.db.models import Sum

import datetime
from django.utils import timezone


class Question(models.Model):
    question_id = models.BigAutoField(primary_key=True, editable=False)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    opened = models.BooleanField(default=True)

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

    def total_votes(self):
        """Calculates the total number of votes for this poll."""
        return self.choice_set.aggregate(Sum('votes'))['votes__sum']


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_id = models.BigAutoField(primary_key=True, editable=False)

    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

    def votes_percentage(self):
        """Calculates the percentage of votes for this choice."""
        total = self.question.total_votes()
        return self.votes / float(total) * 100 if total > 0 else 0
