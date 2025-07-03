from rest_framework import serializers

from catalogue.models import MaterialCatalogue



class MaterialCatalogueSerializer(serializers.ModelSerializer):
    class Meta:
        model=MaterialCatalogue
        fields='__all__'

from user_role.models import User, UpcyclerClothesRequest


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UpcyclerClothesRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = UpcyclerClothesRequest
        fields = '__all__'






