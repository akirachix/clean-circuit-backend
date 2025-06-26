# from django import render
from user_role.models import User, Material
from rest_framework import viewsets
from .serializers import (
     MaterialSerializer, UserSerializer,
)
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
