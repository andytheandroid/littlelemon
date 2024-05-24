from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from inventory.forms import InventoryLoginForm


# Create your views here.

def inventory(request):
    return render(request, 'restaurantAdmin.html', {})


def login_user(request):
    if request.method == 'GET':
        form = InventoryLoginForm()
        context = {'form': form}
        return render(request, 'inventorylogin.html', context)
    elif request.method == "POST":
        form = InventoryLoginForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=name, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/inventory/admin/')

    return HttpResponseRedirect('/inventory/adminLogin/?login=fail')


@permission_classes([IsAuthenticated])
def loginInventory(request):
    return render(request, 'inventorylogin.html', {})
