from rest_framework import serializers
from upcycler.models import UpcycledProduct
from upcycler.models import Upcycler
class UpcycledProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=UpcycledProduct
        fields = '__all__'

class UpcyclerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Upcycler
        fields='__all__'