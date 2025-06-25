from django.db import models

# Create your models here.
from django.db import models

class Upcycler(models.Model):
    upcycler = models.AutoField(primary_key=True) 
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True) 
    phone = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class UpcyclerClothesRequest(models.Model):
    request = models.AutoField(primary_key=True)  
    upcycler = models.ForeignKey(Upcycler, on_delete=models.CASCADE) 
    type = models.CharField(max_length=50) 
    quantity = models.IntegerField()  
    requested_at = models.DateTimeField(auto_now_add=True)  
    image = models.ImageField(upload_to='clothes_request_images/', null=True, blank=True)

    def __str__(self):
        return f"{self.type} request by {self.upcycler.name}"
    

class UpcycledProduct(models.Model):
    upcycled_clothes = models.CharField(max_length=50, unique=True)  
    upcycler = models.ForeignKey('Upcycler', on_delete=models.CASCADE)  
    quantity = models.IntegerField() 
    type = models.CharField(max_length=50) 
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2) 
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.upcycled_clothes
