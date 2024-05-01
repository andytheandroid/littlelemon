from rest_framework import serializers
from restaurant.models import MenuItem


class MenuItemSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    Title = serializers.CharField(max_length=255)
    Price = serializers.DecimalField(max_digits=10,decimal_places=2)
    Inventory = serializers.IntegerField()
    class Meta:
     model = MenuItem
     fields = '__all__' 