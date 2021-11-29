from django.urls import path
from . import views
from rest_framework.views import APIView

# app_name ="comments"
urlpatterns = [
    path('Comments', views.CommentList.as_view()),
    path('comments/<int:pk>/', views.CommentDetail.as_view()),
    path('comments/<slug:video_id>/', views.VideoComments.as_view()),
]
     

 