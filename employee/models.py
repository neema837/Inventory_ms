from django.db import models
from company.models import *
from django.utils import timezone

# Create your models here.
#Employ table
class Employdata(models.Model):
    empname=models.CharField(max_length=20)
    empmail=models.EmailField()
    empphone=models.BigIntegerField()
    emppwd=models.CharField(max_length=20,null=True,blank=True)
    status=models.BooleanField(default=False)
    designation=models.CharField(max_length=20,null=True,blank=True)
    cmpid=models.ForeignKey(Companies,on_delete=models.CASCADE,null=True,blank=True)

class Tasks(models.Model):
    taskname=models.CharField(max_length=20)
    taskdesc=models.CharField(max_length=20)
    assigndate=models.DateField(default=timezone.now)
    duedate=models.DateField()
    timeofcomp=models.TimeField()
    priority=models.CharField(max_length=20,null=True,blank=True)
    status=models.BooleanField(default=False)
    empid=models.ForeignKey(Employdata,on_delete=models.CASCADE)
    cmpid=models.ForeignKey(Companies,on_delete=models.CASCADE,null=True,blank=True)
   
#Product category table adding using modal
class ProductCategory(models.Model):
   catname=models.CharField(max_length=20)
   catimage=models.FileField(upload_to="category imgs",null=True,blank=True)
   cmpid=models.ForeignKey(Companies,on_delete=models.CASCADE)

   def __str__(self):
        return self.catname
#Product Table
class Product(models.Model):
    cprodname=models.CharField(max_length=20)
    cproddesc=models.CharField(max_length=50)
    #cprodcatgry=models.CharField(max_length=20)
    cprodbrand=models.CharField(max_length=20,null=True,blank=True)
    cprodprice=models.BigIntegerField(null=True,blank=True)
    cprodminqty=models.BigIntegerField(null=True,blank=True)
    cprodmaxqty=models.BigIntegerField(null=True,blank=True)
    cprodstock=models.BigIntegerField(null=True,blank=True)
    cprodimage=models.FileField(upload_to="product imgs")
    cpaddingdate=models.DateField(null=True,blank=True)
    cpexpdate=models.DateField(null=True,blank=True)
    cprodcat=models.ForeignKey(ProductCategory,on_delete=models.CASCADE,null=True,blank=True)
    cmpid=models.ForeignKey(Companies,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.cprodname
