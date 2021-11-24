from django.urls import path
from . import views
from rest_framework.views import APIView


# app_name ="replies"
urlpatterns = [
     path('Replies', views.RepliesList.as_view()),
     

 ]