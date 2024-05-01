from django.shortcuts import render




from rest_framework.decorators import api_view
from rest_framework.generics import *
from rest_framework.viewsets import ModelViewSet
from .models import MenuItem
from .models import Booking
from .serializers import MenuItemSerializer, BookingSerializer


def index(request):
  return render(request, 'index.html', {})


# Create your views here. 
class MenuItemsView(ListCreateAPIView):
  queryset = MenuItem.objects.all()
  serializer_class = MenuItemSerializer

class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
  queryset = MenuItem.objects.all()
  serializer_class = MenuItemSerializer

class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
