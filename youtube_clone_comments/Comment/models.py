from django.db import models

# Create your models here.
class Comment(models.Model):
    like = models.IntegerField(default=0),
    dislike = models.IntegerField(default=0),
    commentText = models.TextField(max_length=150),
    videoId = models.CharField(max_length=16)