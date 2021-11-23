from django.db import models

# Create your models here.
class Reply(models.Model):    
    commentId = models.TextField(max_length=150)

    # connect primary key with foreign key
