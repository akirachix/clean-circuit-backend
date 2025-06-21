from django.contrib import admin

# Register your models here.

from .models import PaymentDetails
admin.site.register(PaymentDetails)