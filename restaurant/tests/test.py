from django.test import TestCase

from restaurant.models import MenuItem

class MenuTest(TestCase):

    def setUp(self):
       MenuItem.objects.create(Title="Pizza", Price=20, Inventory=10)
       MenuItem.objects.create(Title="Sandwich", Price=8, Inventory=30)


    def test_get_item(self):
         item = MenuItem.objects.create(Title="IceCream", Price=80, Inventory=100)
         print(item.Title)
         self.assertEqual(item.Title, "IceCream")

    def test_get_all(self):
        pizza = MenuItem.objects.get(Title="Pizza")
        sandwich = MenuItem.objects.get(Title="Sandwich")
        self.assertEqual(pizza.Title, "Pizza")
        self.assertEqual(sandwich.Title, "Sandwich")