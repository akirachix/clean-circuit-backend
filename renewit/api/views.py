from django.shortcuts import render
from rest_framework import viewsets
from upcycledproducts.models import UpcycledProduct
from .serializers import UpcycledProductSerializer

class UpcycledProductViewSet(viewsets.ModelViewSet):
    queryset=UpcycledProduct.objects.all()
    serializer_class= UpcycledProductSerializer



 
