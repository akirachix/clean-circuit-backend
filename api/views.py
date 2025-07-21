from rest_framework import viewsets,generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from user_role.models import User as AppUser, UpcyclerClothesRequest
from payment.models import PaymentDetails
from Material.models import Material
from upcycledproducts.models import UpcycledProduct
from catalogue.models import MaterialCatalogue
from .serializers import (
    AppUserSerializer, UpcyclerClothesRequestSerializer, 
    MaterialSerializer, UpcycledProductSerializer, MaterialCatalogueSerializer,
    PaymentDetailsSerializer, RegistrationSerializer,        
    STKPushSerializer)
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from payment.models import PaymentDetails
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import logging
from datetime import datetime
from .daraja import DarajaAPI
from rest_framework.decorators import api_view





class AppUserViewSet(viewsets.ModelViewSet):
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer
    permission_classes = [AllowAny] 

class UpcyclerClothesRequestViewSet(viewsets.ModelViewSet):
    queryset = UpcyclerClothesRequest.objects.all()
    serializer_class = UpcyclerClothesRequestSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return UpcyclerClothesRequest.objects.filter(upcycler__user=self.request.user)
        return UpcyclerClothesRequest.objects.none()

    def perform_create(self, serializer):
        app_user = AppUser.objects.get(user=self.request.user)
        serializer.save(upcycler=app_user)


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = PaymentDetails.objects.all()
    serializer_class = PaymentDetailsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            app_user = AppUser.objects.get(user=self.request.user)
            # Show only payments associated with this user
            return PaymentDetails.objects.filter(
                models.Q(trader=app_user) | models.Q(upcycler=app_user)
            )
        return PaymentDetails.objects.none()

    def perform_create(self, serializer):
        app_user = AppUser.objects.get(user=self.request.user)
        # Save payment as trader or upcycler, based on user role
        if app_user.role == 'trader':
            serializer.save(trader=app_user)
        elif app_user.role == 'upcycler':
            serializer.save(upcycler=app_user)
        else:
            raise serializers.ValidationError("Invalid role for payment creation.")


class MaterialCatalogueViewSet(viewsets.ModelViewSet):
    queryset = MaterialCatalogue.objects.all()
    serializer_class = MaterialCatalogueSerializer
    permission_classes = [IsAuthenticated]

class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            app_user = AppUser.objects.get(user=self.request.user)
            if app_user.role == 'trader':
                return Material.objects.filter(trader=app_user)
        return Material.objects.none()

    def perform_create(self, serializer):
        app_user = AppUser.objects.get(user=self.request.user)
        if app_user.role == 'trader':
            serializer.save(trader=app_user)
        else:
            raise serializers.ValidationError("Only traders can list materials.")


class UpcycledProductViewSet(viewsets.ModelViewSet):
    queryset = UpcycledProduct.objects.all()
    serializer_class = UpcycledProductSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            app_user = AppUser.objects.get(user=self.request.user)
            if app_user.role == 'upcycler':
                return UpcycledProduct.objects.filter(upcycler=app_user)
        return UpcycledProduct.objects.none()

    def perform_create(self, serializer):
        app_user = AppUser.objects.get(user=self.request.user)
        if app_user.role == 'upcycler':
            serializer.save(upcycler=app_user)
        else:
            raise serializers.ValidationError("Only upcyclers can create upcycled products.")



class STKPushView(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[AllowAny]
    def post(self, request):
        serializer = STKPushSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            daraja = DarajaAPI()
            response = daraja.stk_push(
                phone_number=data['phone_number'],
                amount=data['amount'],
                account_reference=data['account_reference'],
                transaction_desc=data['transaction_desc']
            )
            return Response(response)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RegisterView(generics.CreateAPIView):
    serializer_class = RegistrationSerializer
    permission_classes = [AllowAny]




@api_view(['POST'])
def daraja_callback(request): 
    print("Daraja Callback Data:", request.data)
   
    return Response({"ResultCode": 0, "ResultDesc": "Accepted"})










