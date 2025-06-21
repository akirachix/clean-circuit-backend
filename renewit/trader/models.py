from django.db import models

# Create your models here.
class Trader(models.Model):
    trader = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    phone_number = models.CharField(max_length=50)
    created_at = models.DateTimeField()

    def __str__(self):
        return self.name 

class Material(models.Model):
    material = models.AutoField(primary_key=True)
    trader = models.ForeignKey(Trader, on_delete=models.CASCADE) 
    type = models.CharField(max_length=50)
    quantity = models.IntegerField()
    condition = models.CharField(max_length=50)
    listed_at = models.DateTimeField()

    def __str__(self):
        return self.type  
