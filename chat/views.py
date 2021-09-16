from django.shortcuts import render, redirect, reverse
from .models import *
from django.db import IntegrityError


# главная страница
def index(request):
    rooms = Room.objects.all()
    if request.method == "POST":
        room_name = request.POST.get('room_name')
        username = request.POST.get('username')
        try:
            new_room = Room(room_name=room_name)
            new_room.save()
        except IntegrityError:
            new_room = Room.objects.get(room_name=room_name)
            return redirect(reverse(room, args=[new_room.pk, username]))

    return render(request, 'index.html', {'rooms': rooms})


# страница чата
def room(request, room_id, username):
    if username == '':
        return redirect(reverse(index))
    room_obj = Room.objects.get(pk=room_id)
    messages = Message.objects.filter(room=room_obj)
    return render(request, 'room.html', {
        'room': room_obj,
        'room_name': room_obj.room_name,
        'username': username,
        'messages': messages
    })
