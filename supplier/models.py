from django.db import models
from supplier.models import*

# Create your models here.
class Suppliers(models.Model):
    spname=models.CharField(max_length=20)
    spmail=models.EmailField()
    spphno=models.BigIntegerField()
    spaddr=models.CharField(max_length=30)
    spcity=models.CharField(max_length=20)
    spstate=models.CharField(max_length=20)
    spzip=models.CharField(max_length=20)
    spcountry=models.CharField(max_length=20)
    splic=models.FileField(upload_to="slicense")
    sppwd=models.CharField(max_length=20,null=True,blank=True)
    approve=models.BooleanField(default=False)
    reject=models.BooleanField(default=False)
    status=models.CharField(max_length=20,null=True,blank=True)

class SproductCategory(models.Model):
   catname=models.CharField(max_length=20)
   supid=models.ForeignKey(Suppliers,on_delete=models.CASCADE)

   def __str__(self):
        return self.catname
#Product Table
class Sproduct(models.Model):
    sprodname=models.CharField(max_length=20)
    sproddesc=models.CharField(max_length=50)
    sprodbrand=models.CharField(max_length=20,null=True,blank=True)
    sprodprice=models.BigIntegerField(null=True,blank=True)
    sprodminqty=models.BigIntegerField(null=True,blank=True)
    sprodmaxqty=models.BigIntegerField(null=True,blank=True)
    sprodstock=models.BigIntegerField(null=True,blank=True)
    sprodimage=models.FileField(upload_to="sproduct imgs")
    spaddingdate=models.DateField(null=True,blank=True)
    spexpdate=models.DateField(null=True,blank=True)
    sprodcat=models.ForeignKey(SproductCategory,on_delete=models.CASCADE,null=True,blank=True)
    supid=models.ForeignKey(Suppliers,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.sprodname


