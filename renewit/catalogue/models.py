from django.db import models

# Create your models here.
class Catalogue(models.Model):
    MATERIAL_TYPES = [
        ('fabric', 'Fabric'),
        ('metal', 'Metal'),
        ('plastic', 'Plastic'),
        ('wood', 'Wood'),
        ('other', 'Other'),
    ]
    material_type = models.CharField(max_length=50, choices=MATERIAL_TYPES)  
    price_per_kg = models.DecimalField(max_digits=10, decimal_places=2)  
    last_update_date = models.DateField(auto_now=True) 
    material_description = models.TextField(blank=True)  
    created_at = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return f"{self.material_type.capitalize()} - {self.price_per_kg} per kg"

    def calculate_price(self, quantity):
        """Calculate the total price for a given quantity in kg."""
        return self.price_per_kg * quantity
