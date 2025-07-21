from django.db import models
from user_role.models import User

class UpcycledProduct(models.Model):
    upcycled_clothes = models.CharField(max_length=50, unique=True)
    image = models.ImageField(upload_to='upcycled_clothes_images/', null=True, blank=True)
    quantity = models.IntegerField()
    upcycler = models.ForeignKey(User, on_delete=models.CASCADE, related_name='upcycled_products', default=1)
    type = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.upcycled_clothes
