from rest_framework import serializers
from django.contrib.auth.models import User as DjangoUser
from user_role.models import User, UpcyclerClothesRequest
from payment.models import PaymentDetails
from Material.models import Material
from upcycledproducts.models import UpcycledProduct
from catalogue.models import MaterialCatalogue


class DjangoUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True) 
    password = serializers.CharField(write_only=True)

    class Meta:
        model = DjangoUser
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        return DjangoUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )


class RegistrationSerializer(serializers.ModelSerializer):
    user = DjangoUserSerializer()

    class Meta:
        model = User
        fields = ['user', 'name', 'phone', 'role']

    def validate(self, attrs):
        user_data = attrs.get('user')
        user_serializer = DjangoUserSerializer(data=user_data)
        user_serializer.is_valid(raise_exception=True) 
        return super().validate(attrs)

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        django_user = DjangoUserSerializer().create(user_data)
        profile_user = User.objects.create(user=django_user, **validated_data)
        return profile_user


class AppUserSerializer(serializers.ModelSerializer):
    user = DjangoUserSerializer()
    class Meta:
        model = User
        fields = ['id', 'user', 'name','phone', 'role']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        django_user = DjangoUserSerializer().create(user_data)
        return User.objects.create(user=django_user, **validated_data)


    def update(self, instance, validated_data):
        user_data = validated_data.pop("user", None)
        if user_data:
            django_user = instance.user
            django_user.username = user_data.get("username", django_user.username)
            django_user.email = user_data.get("email", django_user.email)
            if user_data.get("password"):
                django_user.set_password(user_data["password"])
            django_user.save()

        for attr in ["name", "email", "phone", "role"]:
            setattr(instance, attr, validated_data.get(attr, getattr(instance, attr)))
        instance.save()
        return instance


class UpcyclerClothesRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = UpcyclerClothesRequest
        fields = '__all__'


class PaymentDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentDetails
        fields = '__all__'


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = '__all__'


class UpcycledProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = UpcycledProduct
        fields = '__all__'


class MaterialCatalogueSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaterialCatalogue
        fields = '__all__'



class STKPushSerializer(serializers.Serializer):
    type = serializers.CharField(max_length=50)
    quantity = serializers.IntegerField()
    condition = serializers.CharField(max_length=50)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    phone_number = serializers.CharField(max_length=15, required=True)
    amount = serializers.DecimalField(max_digits=10, decimal_places=2, required=True)
    account_reference = serializers.CharField(max_length=100, required=True)
    transaction_desc = serializers.CharField(max_length=200, required=True)




class STKPushSerializer(serializers.Serializer):
   phone_number = serializers.CharField()
   amount = serializers.DecimalField(max_digits=10, decimal_places=2)
   account_reference = serializers.CharField(max_length=12, default="TX12345")
   transaction_desc = serializers.CharField()


class DarajaAPISerializer(serializers.Serializer):
   class Meta:
       model= PaymentDetails
       fields= '__all__'

class PaymentSerializer(serializers.ModelSerializer):
   class Meta:
       model = PaymentDetails
       fields =     fields = [
            'status', 'amount',
           'merchant_request_id', 'checkout_request_id', 'result_code',
           'result_desc', 'mpesa_receipt_number', 'phone_number',
           'transaction_date', 'updated_at'
       ]
       read_only_fields= ['payment_id','created_at','updated_at']
