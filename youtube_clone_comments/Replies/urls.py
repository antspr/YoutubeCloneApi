from django.urls import path
from rest_framework.views import APIView
from . import views

urlpatterns = [
    path('replies/', views.ReplyList.as_view()),
    path('replies/<int:pk>/', views.ReplyDetail.as_view()),
]