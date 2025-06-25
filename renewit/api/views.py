from catalogue.models import MaterialCatalogue
from rest_framework import viewsets
from .serializers import MaterialCatalogueSerializer

    
class MaterialCatalogueViewSet(viewsets.ModelViewSet):
    queryset =MaterialCatalogue.objects.all()
    serializer_class=MaterialCatalogueSerializer