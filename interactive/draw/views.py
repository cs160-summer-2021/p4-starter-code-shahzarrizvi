# chat/views.py
from django.shortcuts import render

def like(request):
    return render(request, 'draw/like.html')

def feedback(request):
    return render(request, 'draw/feedback.html')

def comment(request):
    return render(request, 'draw/comment.html')

def index(request):
    return render(request, 'draw/index.html')

def large(request):
    return render(request, 'draw/large.html')

def room(request, room_name):
    return render(request, 'draw/room.html', {
        'room_name': room_name
    })
