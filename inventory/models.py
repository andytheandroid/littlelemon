from django.core.validators import MinValueValidator
from django.db import models


# Create your models here.

class Ingredient(models.Model):
    name = models.CharField(max_length=100)  # Add a name field
    qty = models.DecimalField(max_digits=10, decimal_places=2)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class MenuInventoryItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Purchase(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    amount_purchased = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_date = models.DateTimeField(auto_now_add=True)  # Add a date field

    @property
    def total(self):
        return self.amount_purchased * self.ingredient.unit_price  # Calculate total

    def __str__(self):
        return f"{self.amount_purchased} of {self.ingredient.name}"


class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey('MenuInventoryItem', on_delete=models.CASCADE, related_name='recipe_requirements')
    ingredient = models.ForeignKey('Ingredient', on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=8, decimal_places=2, validators=[MinValueValidator(0)])
