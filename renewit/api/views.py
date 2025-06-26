from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from upcycler.models import UpcycledProduct
from upcycler.models import Upcycler
from .serializers import (UpcycledProductSerializer,UpcyclerSerializer)

class UpcycledProductViewSet(viewsets.ModelViewSet):
    queryset=UpcycledProduct.objects.all()
    serializer_class= UpcycledProductSerializer

class UpcyclerViewSet(viewsets.ModelViewSet):
    queryset=Upcycler.objects.all()
    serializer_class=UpcyclerSerializer
 