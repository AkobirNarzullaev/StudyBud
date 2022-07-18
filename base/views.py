from django.shortcuts import render, redirect
from .models import Room, Topic
from django.db.models import Q
from .forms import RoomForm

# rooms = [
#     {'id' : 1, 'name': 'Lets learn Python!'},
#     {'id' : 2, 'name': 'Design with me!'},
#     {'id' : 3, 'name': 'Frontend development'},
# ]


def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(
        Q(topic__name__icontains = q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
    )

    topics = Topic.objects.all()
    room_count = rooms.count()

    context = {'rooms' : rooms, 'topics': topics, 'room_count': room_count}
    return render(request, 'base/home.html', context) #instead of context we can just pass in above dictionary

def room(request, pk):
    room = Room.objects.get(id=pk) #In order to make the id  unique we are gonna pass in pk(primary key)
    room = None         #room is set to None because at first there will be no rooms
    return render(request, 'base/room.html')

def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")


    context = {'form': form}
    return render(request, 'base/room_form.html', context)

def updateRoom(request, pk):
    room = Room.objects.get(id=pk) #update the room by id
    form = RoomForm(instance=room)

    if request.method == 'POST':
        form = RoomForm(request.POST, instance = room)
        if form.is_valid():
            form.save()
            return redirect("home")

    context = {'form': form}
    return render(request, 'base/room_form.html', context)

def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': room})