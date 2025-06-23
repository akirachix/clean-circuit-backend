from django.db import models

# Create your models here.
class PaymentDetails(models.Model):
    payment_id = models.CharField(max_length=255, primary_key=True)
    trader_id = models.ForeignKey( 'trader.Trader',on_delete=models.CASCADE)
    upcycler_id = models.ForeignKey('upcycler.Upcycler',on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    quantity = models.IntegerField()
    condition = models.CharField(max_length=50)
    listed_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return f"PaymentDetails(payment_id={self.payment_id}, trader_id={self.trader_id}, upcycler_id={self.upcycler_id}, type={self.type}, quantity={self.quantity}, condition={self.condition}, listed_at={self.listed_at}, price={self.price})"