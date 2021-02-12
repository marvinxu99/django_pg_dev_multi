from django.db import models
from django.urls import reverse


class Event(models.Model):
    title = models.CharField(max_length=200)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

    @property
    def get_html_url(self):
        url = reverse('utils:event_edit', args=(self.id,))
        #return f'<p>{self.title}</p><a href="{url}">edit</a>'
        return f'<a href="{url}"> {self.title} </a>'
