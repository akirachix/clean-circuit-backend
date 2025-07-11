from rest_framework import serializers

from upcycledproducts.models import UpcycledProduct
from user_role.models import UpcyclerClothesRequest


from Material.models import Material



from catalogue.models import MaterialCatalogue


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = '__all__'


class MaterialCatalogueSerializer(serializers.ModelSerializer):
    class Meta:
        model=MaterialCatalogue
        fields='__all__'

class UpcycledProductSerializer(serializers.ModelSerializer):
    class Meta:

        model = UpcycledProduct
        fields = '__all__'

        model = UpcyclerClothesRequest
        fields = '__all__'






