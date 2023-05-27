from django.db import models
from supplier.models import *

# Create your models here.
class Companies(models.Model):
    cpname=models.CharField(max_length=20)
    cpmail=models.EmailField()
    cpphno=models.BigIntegerField()
    cpaddr=models.CharField(max_length=30)
    cpcity=models.CharField(max_length=20)
    cpzip=models.CharField(max_length=20)
    cpstate=models.CharField(max_length=20)
    cpcountry=models.CharField(max_length=20)
    cptype=models.CharField(max_length=20)
    cplic=models.FileField(upload_to="clicense")
    cplogo=models.FileField(upload_to="clogo",null=True,blank=True)
    cppwd=models.CharField(max_length=20,null=True,blank=True)
    status=models.BooleanField(default=False)
    approve=models.BooleanField(default=False)
    reject=models.BooleanField(default=False)

    def __str__(self):
        return self.cpname

    














