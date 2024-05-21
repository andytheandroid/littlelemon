from django.shortcuts import render
from rest_framework.authtoken.admin import User
from rest_framework.decorators import api_view
from rest_framework.generics import *
from rest_framework.viewsets import ModelViewSet
from .models import MenuItem
from .models import Booking
from .serializers import MenuItemSerializer, BookingSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import login, authenticate

from .forms import BookingForm, LoginForm, SignUpForm


def index(request):
    return render(request, 'index.html', {})


def about(request):
    return render(request, 'about.html', {})


def book(request):
    return render(request, 'booking.html', {})


def book_table(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            number_of_guests = form.cleaned_data['number_of_guests']
            reservation_date = form.cleaned_data['reservation_date']
            reservation = Booking(Name=name, No_of_guests=number_of_guests, BookingData=reservation_date)
            reservation.save()
            return HttpResponseRedirect('/restaurant/?booking=success')
    else:
        form = BookingForm()  # Initialize an empty form for GET requests

    context = {'form': form}
    return render(request, 'booking.html', context)


def login_user(request):
    if request.method == 'GET':
        form = LoginForm()
        context = {'form': form}
        return render(request, 'login.html', context)
    elif request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=name, password=password)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/restaurant/?login=success')

    return HttpResponseRedirect('/restaurant/?login=fail')


def sign_up_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/restaurant/?registration=success')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


class MenuItemsView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class BookingViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class MenuItemViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


@api_view()
@permission_classes([IsAuthenticated])
# @authentication_classes([TokenAuthentication])
def msg(request):
    return request.response({"message": "This view is protected"})
