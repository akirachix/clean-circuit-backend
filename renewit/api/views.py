from upcycler.models import Upcycler, UpcyclerClothesRequest, UpcycledProduct
from rest_framework import viewsets
from .serializers import (
    UpcyclerSerializer, UpcyclerClothesRequestSerializer, UpcycledProductSerializer,
    
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
