from rest_framework import serializers
from upcycler.models import Upcycler, UpcyclerClothesRequest, UpcycledProduct
from trader.models import Trader, Material
from payment.models import PaymentDetails
from catalogue.models import Catalogue


class UpcyclerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Upcycler
        fields = '__all__'

class UpcyclerClothesRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = UpcyclerClothesRequest
        fields = '__all__'

class UpcycledProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = UpcycledProduct
        fields = '__all__'

class TraderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trader
        fields = '__all__'

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentDetails
        fields = '__all__'

class CatalogueSerializer(serializers.ModelSerializer):
    class Meta:
        model=Catalogue
        fields='__all__'

