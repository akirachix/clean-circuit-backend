from user_role.models import User, UpcyclerClothesRequest
from rest_framework import viewsets
from .serializers import (
     UserSerializer, UpcyclerClothesRequestSerializer
    
)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UpcyclerClothesRequestViewSet(viewsets.ModelViewSet):
    queryset = UpcyclerClothesRequest.objects.all()
    serializer_class = UpcyclerClothesRequestSerializer

