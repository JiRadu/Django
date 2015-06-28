from django.db import models
from django.utils import timezone

class Post(models.Model):
    actors = models.TextField()
    title = models.CharField(max_length=200)
    summary = models.TextField()
    release_date = models.DateField(blank=True, null=True)
    image = models.ImageField(upload_to='./static/media/')

    def __str__(self):
        return self.title

