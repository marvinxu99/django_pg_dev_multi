import datetime
from django.urls import reverse
from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    # def __str__(self):
    #     return self.title

    # @property
    # def get_html_url(self):
    #     url = reverse('event_edit', args=(self.id,))
    #     return f'<p>{self.title}</p><a href="{url}">edit</a>'