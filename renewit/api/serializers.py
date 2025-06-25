from rest_framework import serializers
from catalogue.models import MaterialCatalogue



class MaterialCatalogueSerializer(serializers.ModelSerializer):
    class Meta:
        model=MaterialCatalogue
        fields='__all__'

