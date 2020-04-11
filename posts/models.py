from django.db import models
from django.conf import settings


class Post(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')  # Use FileField for a regular file.
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title