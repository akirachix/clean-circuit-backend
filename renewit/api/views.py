
from payment.models import PaymentDetails
from rest_framework import viewsets
from .serializers import ( PaymentSerializer)

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = PaymentDetails.objects.all()
    serializer_class = PaymentSerializer
    
