from django.shortcuts import render




from rest_framework.decorators import api_view
from rest_framework.generics import *
from .models import MenuItem
from .serializers import MenuItemSerializer


def index(request):
  return render(request, 'index.html', {})


# Create your views here. 
class MenuItemsView(ListCreateAPIView):
  queryset = MenuItem.objects.all()
  serializer_class = MenuItemSerializer

class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
  queryset = MenuItem.objects.all()
  serializer_class = MenuItemSerializer