from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib import messages


from inventory.forms import InventoryLoginForm, IngredientsForm
from inventory.models import Ingredient


# Create your views here.

def inventory(request):
    form = IngredientsForm()
    context = {'form': form}
    if request.method == 'GET':

        return render(request, 'restaurantAdmin.html', context)

    if request.method == 'POST':
        form = IngredientsForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            qty = form.cleaned_data['qty']
            unit_price = form.cleaned_data['unitary_price']
            ingredient = Ingredient(name=name, qty=qty, unit_price=unit_price)
            ingredient.save()
            messages.success(request, f"Ingredient '{name}' added successfully!")
            return render(request, 'restaurantAdmin.html',{"form": form})

        else:

            messages.error(request, "Please correct the errors in the form.")
            return render(request, 'restaurantAdmin.html',{form:form})


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
