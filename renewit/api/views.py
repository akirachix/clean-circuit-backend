<<<<<<< HEAD
from catalogue.models import MaterialCatalogue
from rest_framework import viewsets, status
from .serializers import MaterialCatalogueSerializer
from rest_framework.response import Response

class MaterialCatalogueViewSet(viewsets.ModelViewSet):
    queryset = MaterialCatalogue.objects.all()
    serializer_class = MaterialCatalogueSerializer
    
def create(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    
    
    if serializer.is_valid():
        
        validated_data = serializer.validated_data
      
        obj, created = MaterialCatalogue.objects.update_or_create(
            material_type=validated_data['material_type'],
            defaults=validated_data
        )
        
     
        serializer = self.get_serializer(obj)
        
      
        if created:
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_200_OK)
    
  
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
=======
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

>>>>>>> 4722806222f7690e4608f673b166fe14b3397831
