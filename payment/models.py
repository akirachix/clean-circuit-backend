from django.db import models
from user_role.models import User

class PaymentDetails(models.Model):
    type = models.CharField(max_length=50)
    quantity = models.IntegerField()
    condition = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    listed_at = models.DateTimeField(auto_now_add=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    account_reference = models.CharField(max_length=100, null=True, blank=True)
    transaction_desc = models.CharField(max_length=255, null=True, blank=True)
    payment_status = models.CharField(max_length=30, null=True, blank=True)
    mpesa_checkout_id = models.CharField(max_length=100, null=True, blank=True, unique=True)
    mpesa_receipt_number = models.CharField(max_length=50, null=True, blank=True)
    transaction_date = models.DateTimeField(null=True, blank=True)
    result_code = models.CharField(max_length=10, null=True, blank=True)
    result_description = models.CharField(max_length=200, null=True, blank=True)
    phone_number_from_callback = models.CharField(max_length=15, null=True, blank=True)
    amount_from_callback = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    trader = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='payments_as_trader',
        limit_choices_to={'role': 'trader'},
        null=True, blank=True
    )
    upcycler = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='payments_as_upcycler',
        limit_choices_to={'role': 'upcycler'},
        null=True, blank=True
    )
  

    def clean(self):
        from django.core.exceptions import ValidationError
        if self.trader and self.trader.role != 'trader':
            raise ValidationError({'trader': 'Selected user is not a trader.'})
        if self.upcycler and self.upcycler.role != 'upcycler':
            raise ValidationError({'upcycler': 'Selected user is not an upcycler.'})
