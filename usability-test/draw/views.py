# chat/views.py
from django.shortcuts import render

def likeA(request):
    return render(request, 'draw/likeA.html')

def feedbackA(request):
    return render(request, 'draw/feedbackA.html')

def commentA(request):
    return render(request, 'draw/commentA.html')

def likeB(request):
    return render(request, 'draw/likeB.html')

def feedbackB(request):
    return render(request, 'draw/feedbackB.html')

def commentB(request):
    return render(request, 'draw/commentB.html')

def index(request):
    return render(request, 'draw/index.html')

def large(request):
    return render(request, 'draw/large.html')

def room(request, room_name):
    return render(request, 'draw/room.html', {
        'room_name': room_name
    })
