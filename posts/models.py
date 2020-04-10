from django.db import models

class Post(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')  # Use FileField for a regular file.

    def __str__(self):
        return self.title