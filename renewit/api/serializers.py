from rest_framework import serializers
from upcycledproducts.models import UpcycledProduct

class UpcycledProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = UpcycledProduct
        fields = '__all__'