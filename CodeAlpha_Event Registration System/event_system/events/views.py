from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Event, Registration


def home(request):
    return render(request, 'events/home.html')


def register(request):

    if request.method == 'POST':

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        return redirect('/')

    return render(request, 'events/register.html')

def user_login(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user:
            login(request, user)
            return redirect('/')

    return render(request, 'events/login.html')

def event_list(request):

    search = request.GET.get('search')

    if search:
        events = Event.objects.filter(
            name__icontains=search
        )
    else:
        events = Event.objects.all()

    return render(
        request,
        'events/event_list.html',
        {'events': events}
    )

@login_required
def register_event(request, event_id):

    event = Event.objects.get(id=event_id)

    already_registered = Registration.objects.filter(
        user=request.user,
        event=event
    ).exists()

    if not already_registered:

        Registration.objects.create(
            user=request.user,
            event=event
        )

    return redirect('/events/')

@login_required
def my_registrations(request):

    registrations = Registration.objects.filter(
        user=request.user
    )

    return render(
        request,
        'events/my_registrations.html',
        {'registrations': registrations}
    )

@login_required
def cancel_registration(request, reg_id):

    registration = Registration.objects.get(
        id=reg_id,
        user=request.user
    )

    registration.delete()

    return redirect('/myregistrations/')