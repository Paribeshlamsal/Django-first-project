from django.db import models

class Customer(models.Model):
    name= models.CharField(max_length=100)
    address = models.TextField()
    phone = models.IntegerField()
    
class Car(models.Model):
    car_name=models.CharField(max_length=200)    
    speed=models.IntegerField(default=50)

    def __str__(self):
        return self.car_name
