from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import render, redirect
from pymysql import IntegrityError
from rest_framework import viewsets
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib import messages
from rest_framework.utils import json
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import *
from django.views.generic.edit import UpdateView, DeleteView
from inventory.forms import InventoryLoginForm, IngredientsForm, EditIngredientForm
from inventory.models import Ingredient
from inventory.serializers import IngredientSerializer
from django.http import JsonResponse
from django.urls import reverse_lazy


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
            return render(request, 'restaurantAdmin.html', {"form": form})

        else:

            messages.error(request, "Please correct the errors in the form.")
            return render(request, 'restaurantAdmin.html', {form: form})


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


class IngredientsView(ListCreateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class UpdateIngredients(UpdateView):
    model = Ingredient
    fields = ['name', 'qty', 'unit_price']
    template_name = 'restaurantAdmin.html'


def get_form_class(self):
    return EditIngredientForm


class IngredientDeleteView(DeleteView):
    model = Ingredient
    success_url = "templates/restaurantAdmin.html"


def ingredients_list(request):
    view = IngredientsView.as_view()
    response = view(request)
    ingredients = response.data  # Extract the serialized data
    return render(request, 'restaurantAdmin.html', {'ingredients': ingredients})


def update_ingredient(request, pk):
    if request.method != "PUT":
        return JsonResponse({"error": "Only PUT requests are allowed"}, status=405)  # Method Not Allowed

    try:
        data = json.loads(request.body)
        print(data)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON data"}, status=400)  # Bad Request

    obj = Ingredient.objects.get(pk=data["id"])
    obj.name = data["name"]
    obj.qty = data["quantity"]
    obj.unit_price = data["price"]
    print(obj)

    try:
        obj.save()  # Save the updated object to the database
        return JsonResponse({"message": "Data updated successfully", "data": data}, status=200)
    except IntegrityError as e:
        # Handle unique constraint violations or other DB errors
        return JsonResponse({"error": f"Database error: {str(e)}"}, status=400)
