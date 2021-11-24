from django.shortcuts import render
from .models import Reply
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.views import status
from .serializers import ReplySerializer

# Create your views here.
class RepliesList(APIView):
    #get all the Replies from Video
    def get(self,request):
        replies = Reply.objects.all()
        serializer = ReplySerializer(replies, many= True)
        return Response(serializer.data)

    def post(self, request):
        serializer =ReplySerializer(data=request.data)
        return Response(serializer.data)