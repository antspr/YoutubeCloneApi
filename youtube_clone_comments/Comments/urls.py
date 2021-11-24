from django.urls import path
from . import views
from rest_framework.views import APIView

# app_name ="comments"
urlpatterns = [
     path('Comments', views.CommentsList.as_view()),
     

 ]