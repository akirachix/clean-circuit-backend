from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from user_role.models import UpcycledProduct
from user_role.models import User
from .serializers import (UpcycledProductSerializer,UserSerializer)

class UpcycledProductViewSet(viewsets.ModelViewSet):
    queryset=UpcycledProduct.objects.all()
    serializer_class= UpcycledProductSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer
 
