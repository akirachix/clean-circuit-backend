from django.db import models

# Create your models here.

class User(models.Model):
    ROLE_CHOICES = [
        ('trader', 'Trader'),
        ('upcycler', 'Upcycler'),
    ]
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    phone = models.CharField(max_length=50)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='upcycler')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class UpcycledProduct(models.Model):
    upcycled_clothes = models.CharField(max_length=50, unique=True)  
    user = models.ForeignKey('User', on_delete=models.CASCADE)  
    image=models.ImageField(upload_to='upcycled_clothes_images/', null=True, blank=True)
    quantity = models.IntegerField() 
    type = models.CharField(max_length=50) 
    price = models.DecimalField(max_digits=10, decimal_places=2) 
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.upcycled_clothes