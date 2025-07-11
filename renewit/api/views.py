from django.shortcuts import render
from rest_framework import viewsets
from upcycledproducts.models import UpcycledProduct
from .serializers import UpcycledProductSerializer

from catalogue.models import MaterialCatalogue
from rest_framework import viewsets, status
from .serializers import MaterialCatalogueSerializer
from rest_framework.response import Response

class UpcycledProductViewSet(viewsets.ModelViewSet):
    queryset=UpcycledProduct.objects.all()
    serializer_class= UpcycledProductSerializer

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

