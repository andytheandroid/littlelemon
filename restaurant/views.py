from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.generics import *
from rest_framework.viewsets import ModelViewSet
from .models import MenuItem
from .models import Booking
from .serializers import MenuItemSerializer, BookingSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes


def index(request):
  return render(request, 'index.html', {})

def about(request):
  return render(request, 'about.html', {})

def book(request):
  return render(request, 'booking.html', {})

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
   return request.response({"message":"This view is protected"})
