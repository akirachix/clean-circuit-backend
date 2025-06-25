from rest_framework import serializers
from upcycler.models import Upcycler, UpcyclerClothesRequest, UpcycledProduct


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



