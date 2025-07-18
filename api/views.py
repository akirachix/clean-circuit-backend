from rest_framework import viewsets
from .serializers import ( UserSerializer, UpcyclerClothesRequestSerializer, PaymentSerializer,
                          UpcycledProductSerializer, MaterialSerializer, MaterialCatalogueSerializer)
from user_role.models import User, UpcyclerClothesRequest
from payment.models import PaymentDetails
from upcycledproducts.models import UpcycledProduct
from Material.models import Material
from catalogue.models import MaterialCatalogue

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UpcyclerClothesRequestViewSet(viewsets.ModelViewSet):
    queryset = UpcyclerClothesRequest.objects.all()
    serializer_class = UpcyclerClothesRequestSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = PaymentDetails.objects.all()
    serializer_class = PaymentSerializer

class UpcycledProductViewSet(viewsets.ModelViewSet):
    queryset = UpcycledProduct.objects.all()
    serializer_class = UpcycledProductSerializer

class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer

class MaterialCatalogueViewSet(viewsets.ModelViewSet):
    queryset = MaterialCatalogue.objects.all()
    serializer_class = MaterialCatalogueSerializer
