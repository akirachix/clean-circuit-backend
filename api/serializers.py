from rest_framework import serializers
from user_role.models import User, UpcyclerClothesRequest
from payment.models import PaymentDetails
from upcycledproducts.models import UpcycledProduct
from Material.models import Material
from catalogue.models import MaterialCatalogue

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UpcyclerClothesRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = UpcyclerClothesRequest
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentDetails
        fields = '__all__'

class UpcycledProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = UpcycledProduct
        fields = '__all__'

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = '__all__'

class MaterialCatalogueSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaterialCatalogue
        fields = '__all__'
