from django.db import models

# Create your models here.

class Upcycler(models.Model):
    upcycler = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    phone = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class UpcycledProduct(models.Model):
    upcycled_clothes = models.CharField(max_length=50, unique=True)  
    upcycler = models.ForeignKey('upcycler.Upcycler', on_delete=models.CASCADE,default=1)  
    quantity = models.IntegerField() 
    type = models.CharField(max_length=50) 
    price = models.DecimalField(max_digits=10, decimal_places=2) 
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.upcycled_clothes
