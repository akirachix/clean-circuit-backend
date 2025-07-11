
# from django import render
from Material.models import  Material
from rest_framework import viewsets
from .serializers import MaterialSerializer


class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer


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

