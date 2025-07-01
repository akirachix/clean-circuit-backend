from rest_framework import serializers
from user_role.models import UpcycledProduct
from user_role.models import User
class UpcycledProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=UpcycledProduct
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'
