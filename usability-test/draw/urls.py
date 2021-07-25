# chat/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('likeA/', views.likeA, name='likeA'),
    path('commentA/', views.commentA, name='commentA'),
    path('feedbackA/', views.feedbackA, name='feedbackA'),
    path('likeB/', views.likeB, name='likeB'),
    path('commentB/', views.commentB, name='commentB'),
    path('feedbackB/', views.feedbackB, name='feedbackB'),
    path('', views.index, name='index'),
    path('large/', views.large, name='large'),
    path('<str:room_name>/', views.room, name='room'),

]
