from django.db import models

# Create your models here.

class UpcycledProduct(models.Model):
    upcycled_clothes = models.CharField(max_length=50, unique=True)  
    image=models.ImageField(upload_to='upcycled_clothes_images/', null=True, blank=True)
    quantity = models.IntegerField() 
    type = models.CharField(max_length=50) 
    price = models.DecimalField(max_digits=10, decimal_places=2) 
    updated_at = models.DateTimeField(auto_now=True)