from rest_framework import serializers
from upcycler.models import Upcycler, UpcyclerClothesRequest


class UpcyclerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Upcycler
        fields = '__all__'

class UpcyclerClothesRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = UpcyclerClothesRequest
        fields = '__all__'





