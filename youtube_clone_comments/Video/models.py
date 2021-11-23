from django.db import models

# Create your models here.
class Comment(models.Model):
    userId = int(),
    userName = models.CharField(max_length=50),
    like = models.BooleanField,
    dislike = models.BooleanField,
    reply = models.TextField,