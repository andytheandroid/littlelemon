
from django.db import models;



class Booking(models.Model):
    Name = models.CharField(max_length = 255);
    No_of_guests = models.IntegerField(5);
    BookingData = models.DateField();




class MenuTable(models.Model):
   
    Title = models.CharField(max_length = 255);
    Price = models.DecimalField(max_digits = 10, decimal_places = 10);
    Inventory = models.IntegerField(5);

