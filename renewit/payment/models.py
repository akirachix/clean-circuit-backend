from django.db import models
from user_role.models import User

class PaymentDetails(models.Model):
    type = models.CharField(max_length=50)
    quantity = models.IntegerField()
    condition = models.CharField(max_length=50)
    listed_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    trader = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='payments_as_trader',
        limit_choices_to={'role': 'trader'},
        null=True, blank=True
    )
    upcycler = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='payments_as_upcycler',
        limit_choices_to={'role': 'upcycler'},
        null=True, blank=True
    )

    def __str__(self):
        return f"PaymentDetails(type={self.type}, quantity={self.quantity}, condition={self.condition}, listed_at={self.listed_at}, price={self.price})"

    def clean(self):
        if self.trader and self.trader.role != 'trader':
            raise ValidationError({'trader': 'Selected user is not a trader.'})
        if self.upcycler and self.upcycler.role != 'upcycler':
            raise ValidationError({'upcycler': 'Selected user is not an upcycler.'})
