from django import forms


class InventoryLoginForm(forms.Form):
    username = forms.CharField(label="Your name", max_length=100)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)


class IngredientsForm(forms.Form):
    name = forms.CharField(label="Ingredient", max_length=100)
    qty = forms.IntegerField(label="Number of units")
    unitary_price = forms.IntegerField(label="Price per unit")


class EditIngredientForm(forms.Form):
    ingredientId = forms.HiddenInput()
    ingredientName = forms.CharField(label="Name")
    unitPrice = forms.DecimalField(label="Unit Price", decimal_places=2, min_value=0)
    quantity = forms.IntegerField(label="Quantity", min_value=0)


class MenuItemForm(forms.Form):
    name = forms.CharField(label="Name", max_length=100)
    price = forms.DecimalField(label="Price per unit", decimal_places=2, min_value=0)
    description = forms.CharField(widget=forms.Textarea(attrs={'rows': 10, 'cols': 10}),
                                  )
