from django.shortcuts import render, HttpResponse, redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import User, Room, Topic, Messege
from .forms import RoomFrom, UserFrom, MyUserCreationForm
# Create your views here.

# rooms = [
#     {'id': 1, 'name': "Let's Learn Python"},
#     {'id': 2, 'name': "Let's Learn Django"},
#     {'id': 3, 'name': "Let's Learn C"},
# ]


def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect("Home")

    if request.method == "POST":
        email = request.POST.get('email').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, "User does not found..")
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('Home')
        else:
            messages.error(request, "Password is wrong")
    context = {'page': page}
    return render(request, 'login_reg.html', context)


def logoutuser(request):
    logout(request)
    return redirect("Login")


def registerUser(request):
    page = 'register'
    form = MyUserCreationForm()
    if request.method == "POST":
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect("Home")
        else:
            messages.error(request, 'Something Went Wrong..')
    return render(request, 'login_reg.html', {'page': page, 'form': form})


def hello(request):
    # if request.user.is_authenticated:
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) | Q(name__icontains=q) | Q(description__icontains=q))
    room_count = rooms.count()
    topics = Topic.objects.all()[0:5]
    # rooms = Room.objects.all()
    room_messages = Messege.objects.filter(
        Q(room__topic__name__icontains=q))
    contex = {'rooms': rooms, 'topics': topics,
              'room_count': room_count, "room_messages": room_messages}
    return render(request, 'OLD/index_old.html', contex)
    # else:
    #     return redirect("Login")


def room(request, pk):
    rooms = Room.objects.get(id=pk)
    room_messages = rooms.messege_set.all()
    participants = rooms.participants.all()

    if request.method == "POST":
        messege = Messege.objects.create(
            user=request.user,
            room=rooms,
            body=request.POST.get("body")
        )
        rooms.participants.add(request.user)
        return redirect('Room', pk=rooms.id)

    contex = {'room': rooms, 'room_messages': room_messages,
              'participants': participants}
    return render(request, 'room.html', contex)


def userProfile(request, pk):
    user = User.objects.get(id=pk)
    rooms = user.room_set.all()
    room_messages = user.messege_set.all()
    topics = Topic.objects.all()
    context = {"user": user, 'rooms': rooms,
               'room_messages': room_messages, 'topics': topics}
    return render(request, 'profile.html', context)


@login_required(login_url='/login')
def create_room(request):
    form = RoomFrom()
    topics = Topic.objects.all()
    context = {'form': form, 'topics': topics}
    if request.method == "POST":
        topic_name = request.POST.get('topic')
        topic, created = Topic.objects.get_or_create(name=topic_name)
        Room.objects.create(
            host=request.user,
            topic=topic,
            name=request.POST.get("name"),
            description=request.POST.get("description")
        )
        return redirect('Home')
    return render(request, 'room_form.html', context)


@login_required(login_url='/login')
def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomFrom(instance=room)
    topics = Topic.objects.all()
    context = {'form': form, 'topics': topics, 'room': room}
    if request.user != room.host:
        return HttpResponse("You are not allow here!!")
    if request.method == "POST":
        topic_name = request.POST.get('topic')
        topic, created = Topic.objects.get_or_create(name=topic_name)
        room.name = request.POST.get('name')
        room.topic = topic
        room.description = request.POST.get('description')
        room.save()
        return redirect('Home')

    return render(request, 'room_form.html', context)


def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)

    if request.user != room.host:
        return HttpResponse("You are not allow here!!")

    if request.method == "POST":
        room.delete()
        return redirect('Home')
    return render(request, 'delete.html', {'obj': room})


def deleteMessege(request, pk):
    messege = Messege.objects.get(id=pk)

    if request.user != messege.user:
        return HttpResponse("You are not allow here!!")

    if request.method == "POST":
        messege.delete()
        return redirect('Home')
    return render(request, 'delete.html', {'obj': messege})


@login_required(login_url='/login')
def updateUser(request):
    user = request.user
    form = UserFrom(instance=user)
    if request.method == "POST":
        form = UserFrom(request.POST, request.FILES, instance=user)
        if form.is_valid:
            form.save()
            return redirect('UserProfile', pk=user.id)
    return render(request, 'update-user.html', {'form': form})


def topicPage(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    topics = Topic.objects.filter(name__icontains=q)
    return render(request, 'topics.html', {"topics": topics})


def activityPage(request):
    room_messages = Messege.objects.all()
    return render(request, 'activity.html', {"room_messages": room_messages})
