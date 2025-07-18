from django.db import models
from datetime import datetime


# Create your models here.
class MaterialCatalogue(models.Model):
    MATERIAL_TYPES = [
        ('cotton', 'Cotton'),
        ('denim', 'Denim'),
        ('polyester', 'Polyester'),
        ('linel', 'Linel'),
        ('satin','Satin'),
        ('silk','Silk'),
        ('wool','Wool'),
    ]

    MATERIAL_PRICES = {
        'cotton':2000.00,  
        'denim': 1000.00,   
        'polyester':200.00,  
        'linel':1500.00,    
        'satin':1500.00,    
        'silk':1500.00,
        'wool':900.00,
    }

    material_type = models.CharField(max_length=50, choices=MATERIAL_TYPES)  
    price_per_kg = models.DecimalField(max_digits=10, decimal_places=2, editable=False)  
    last_update_date = models.DateField(auto_now=True) 
    material_description = models.TextField(blank=True)  
    created_at = models.DateTimeField(auto_now_add=True) 
  

    def __str__(self):
        return f"{self.material_type.capitalize()} - {self.price_per_kg} per kg"

    def save(self, *args, **kwargs):
      
        if self.material_type in self.MATERIAL_PRICES:
            self.price_per_kg = self.MATERIAL_PRICES[self.material_type]
        super().save(*args, **kwargs)

    def calculate_price(self, quantity):
        
        return self.price_per_kg * quantity

