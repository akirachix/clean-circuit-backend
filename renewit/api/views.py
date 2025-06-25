from upcycler.models import Upcycler, UpcyclerClothesRequest, UpcycledProduct
from trader.models import Trader, Material
from payment.models import PaymentDetails
from catalogue.models import Catalogue
from rest_framework import viewsets
from .serializers import (
    UpcyclerSerializer, UpcyclerClothesRequestSerializer, UpcycledProductSerializer,
    TraderSerializer, MaterialSerializer, PaymentSerializer,CatalogueSerializer
)

class UpcyclerViewSet(viewsets.ModelViewSet):
    queryset = Upcycler.objects.all()
    serializer_class = UpcyclerSerializer

class UpcyclerClothesRequestViewSet(viewsets.ModelViewSet):
    queryset = UpcyclerClothesRequest.objects.all()
    serializer_class = UpcyclerClothesRequestSerializer

class UpcycledProductViewSet(viewsets.ModelViewSet):
    queryset = UpcycledProduct.objects.all()
    serializer_class = UpcycledProductSerializer

class TraderViewSet(viewsets.ModelViewSet):
    queryset = Trader.objects.all()
    serializer_class = TraderSerializer

class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = PaymentDetails.objects.all()
    serializer_class = PaymentSerializer
    
class CatalogueViewSet(viewsets.ModelViewSet):
    queryset =Catalogue.objects.all()
    serializer_class=CatalogueSerializer