from rest_framework import serializers

from .models import Ingredient, MenuInventoryItem


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'name', 'qty', 'unit_price']


class MenuInventoryItem(serializers.ModelSerializer):
    class Meta:
        model = MenuInventoryItem
        fields = ['id', 'name', 'price', 'description']
