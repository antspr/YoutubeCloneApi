from django.http.response import Http404
from django.shortcuts import render
from .models import Comment
from .serializers import CommentsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status

# Create your views here.
class CommentList(APIView):

    def get(self, request):
        comment = Comment.objects.all()
        serializer = CommentsSerializer(comment, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CommentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CommentDetail(APIView):
    
    def get_comment(self, pk):
        try:
           return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            raise Http404 

    def get(self, request, pk):
        comment = self.get_comment(pk)
        serializer = CommentsSerializer(comment)
        return Response(serializer.data)

    def put(self, request, pk):
        comment = self.get_comment(pk)
        serializer = CommentsSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        comment = self.get_comment(pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class VideoComments(APIView):

    def get(self, request, video_id):
        comments = Comment.objects.filter(video_id__exact=video_id)
        serializer = CommentsSerializer(comments, many=True)
        return Response(serializer.data)







        