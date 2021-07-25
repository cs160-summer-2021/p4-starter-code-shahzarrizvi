# chat/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('comment/', views.comment, name='comment'),
    path('feedback/', views.feedback, name='feedback'),
    path('', views.index, name='index'),
    path('large/', views.large, name='large'),
    path('<str:room_name>/', views.room, name='room'),

]
