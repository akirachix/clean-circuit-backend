from upcycler.models import Upcycler, UpcyclerClothesRequest, UpcycledProduct
from rest_framework import viewsets
from .serializers import (
    UpcyclerSerializer, UpcyclerClothesRequestSerializer,
    
)

class UpcyclerViewSet(viewsets.ModelViewSet):
    queryset = Upcycler.objects.all()
    serializer_class = UpcyclerSerializer

class UpcyclerClothesRequestViewSet(viewsets.ModelViewSet):
    queryset = UpcyclerClothesRequest.objects.all()
    serializer_class = UpcyclerClothesRequestSerializer

