from django.db import models

# Create your models here.
# class Registeration(models.Model):
#    name=models.CharField(max_length=20)
#    email=models.EmailField()
#    password=models.CharField(max_length=20)
class Admindata(models.Model):
    adname=models.CharField(max_length=20)
    admail=models.EmailField()
    adpwd=models.CharField(max_length=50)

    def __str__(self):
         return self.adname