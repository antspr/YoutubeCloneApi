from django.shortcuts import render
from .serializers import CommentSerializer
from .models import Comment
from rest_framework import APIView
from rest_framework.response import Response
from rest_framework.views import status


# Create your views here.

class CommentList(APIView):
    #get all the comments from Video
    def getComments(self,request):
        comments = Comment.objects.all()
        serializer = CommentSerializer.comments(comments, many= True)
        return Response(serializer.data)

    def postComment(self, request):
        serializer =CommentSerializer(data=request.data)
        return Response(serializer.data)
        