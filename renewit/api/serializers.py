from rest_framework import serializers
from payment.models import PaymentDetails

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentDetails
        fields = '__all__'


