from .models import Comment
from rest_framework import serializers

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id','videoId', 'like', 'dislike', 'commentText']
