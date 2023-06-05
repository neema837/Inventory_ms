from django.db import models
from django.utils import timezone
from employee.models import *

# Create your models here.
class Customers(models.Model):
    uname=models.CharField(max_length=20)
    umail=models.EmailField()
    uphone=models.BigIntegerField()
    uimage=models.FileField(upload_to="users")
    uaddr=models.CharField(max_length=30)
    ucity=models.CharField(max_length=20)
    uzip=models.CharField(max_length=20)
    ustate=models.CharField(max_length=20)
    ucountry=models.CharField(max_length=20)
    #utype=models.CharField(max_length=20)
    #ucompany=models.CharField(max_length=20)
    upwd=models.CharField(max_length=20,null=True,blank=True)
    status=models.BooleanField(default=False)



class Cart(models.Model):
    uid=models.ForeignKey(Customers,on_delete=models.CASCADE)
    prodid=models.ForeignKey(Product,on_delete=models.CASCADE,null=True,blank=True)
    uprodqty=models.BigIntegerField(default=1,null=True,blank=True)
    addingdate=models.DateField(default=timezone.now)
    status=models.BooleanField(default=False)


class WishList(models.Model):
    uid=models.ForeignKey(Customers,on_delete=models.CASCADE)
    prodid=models.ForeignKey(Product,on_delete=models.CASCADE,null=True,blank=True)
    waddingdate=models.DateField(default=timezone.now().date())
    status=models.BooleanField(default=False)
    

class NewAddress(models.Model):
    uid=models.ForeignKey(Customers,on_delete=models.CASCADE)
    newaddr=models.CharField(max_length=30)


class Order(models.Model):
    orderid=models.BigIntegerField()
    cartid=models.ManyToManyField(Cart)
    uid=models.ForeignKey(Customers,on_delete=models.CASCADE,null=True,blank=True)
    orderdate=models.DateField(default=timezone.now().date())

    




