from email import message
from email.policy import default
from operator import mod
from django.db import models

# Create your models here.
class Contact(models.Model):
    message = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150,default="")
    email = models.CharField(max_length=150,default="")
    num = models.CharField(max_length=15,default="")
    message = models.TextField(max_length=500,default="")

    def __str__(self) :
        return self.name


class Cars(models.Model):
    car_id = models.AutoField
    car_name = models.CharField(max_length=50)
    desc = models.CharField(max_length=300)
    car_date = models.DateField()
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.car_name

class Order(models.Model):
    car = models.CharField(max_length=150,default="")
    # rent = models.CharField(max_length=10,default="")
    days = models.CharField(max_length=3,default="")

    def __str__(self):
        return self.car
    # def save(self):
    #     self.rent = self.rent * self.days
    #     super(Order,self).save()

   
class Customer(models.Model):
    r_name = models.CharField(max_length=50)
    r_username = models.CharField(max_length=20)
    r_email = models.CharField(max_length=150)
    r_number = models.CharField(max_length=10)
 
    def __str__(self):
        return self.r_name