from django.db import models

# Create your models here.
class PaymentDetails(models.Model):
    type = models.CharField(max_length=50)
    quantity = models.IntegerField()
    condition = models.CharField(max_length=50)
    listed_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return f"PaymentDetails( type={self.type}, quantity={self.quantity}, condition={self.condition}, listed_at={self.listed_at}, price={self.price})"