from django.db import models

# Create your models here.
class Comment(models.Model):
    like = models.IntegerField(null=0)
    dislike = models.IntegerField(null=0)
    commentText = models.CharField(max_length=150)
    videoId = models.CharField(max_length=16, blank=True,null=True)