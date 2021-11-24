from django.shortcuts import render
from .serializers import CommentsSerializer
from .models import Comment
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.views import status


# Create your views here.

class CommentsList(APIView):
    #get all the comments from Video
    def get(self,request):
        comments = Comment.objects.all()
        serializer = CommentsSerializer(comments, many= True)
        return Response(serializer.data)

    def post(self, request):
        serializer =CommentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        