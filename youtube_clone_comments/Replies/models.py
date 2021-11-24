from django.db import models

# Create your models here.
class Reply(models.Model):    
    commentId = models.ForeignKey("Comments.Comment", on_delete=models.CASCADE)
    reply = models.CharField(max_length=1500)

    # connect primary key with foreign key
