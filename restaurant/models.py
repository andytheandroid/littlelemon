from django.db import models


class Booking(models.Model):
    Name = models.CharField(max_length=255)
    No_of_guests = models.IntegerField(5)
    BookingData = models.DateField()


class MenuItem(models.Model):
    Title = models.CharField(max_length=255)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Inventory = models.IntegerField(5)

    def get_item(self):
        return f'{self.title} : {str(self.price)}'
