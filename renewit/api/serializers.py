from rest_framework import serializers
from user_role.models import User, UpcyclerClothesRequest


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UpcyclerClothesRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = UpcyclerClothesRequest
        fields = '__all__'





