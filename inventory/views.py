from django.shortcuts import render
from django.shortcuts import render


# Create your views here.

def inventory(request):
    return render(request, 'restaurantAdmin.html', {})
