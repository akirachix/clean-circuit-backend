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
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from .daraja import DarajaAPI
from rest_framework.decorators import api_view
from django.utils import timezone
from django.db.models import Q
from rest_framework import serializers
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.exceptions import APIException


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
    queryset = PaymentDetails.objects.none()
    serializer_class = PaymentDetailsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            try:
                app_user = AppUser.objects.get(user=self.request.user)
                return PaymentDetails.objects.filter(
                    Q(trader=app_user) | Q(upcycler=app_user)
                )
            except AppUser.DoesNotExist:
                return PaymentDetails.objects.none()
        return PaymentDetails.objects.none()

    def perform_create(self, serializer):
        try:
            app_user = AppUser.objects.get(user=self.request.user)
            if app_user.role == 'trader':
                serializer.save(trader=app_user)
            elif app_user.role == 'upcycler':
                serializer.save(upcycler=app_user)
            else:
                raise serializers.ValidationError("Invalid role for payment creation.")
        except AppUser.DoesNotExist:
            raise serializers.ValidationError("User profile does not exist.")


class MaterialCatalogueViewSet(viewsets.ModelViewSet):
    queryset = MaterialCatalogue.objects.all()
    serializer_class = MaterialCatalogueSerializer
    permission_classes = [IsAuthenticated]

class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    permission_classes = []

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
    authentication_classes = [TokenAuthentication]
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = STKPushSerializer(data=request.data)
        if serializer.is_valid():
            try:
                data = serializer.validated_data
                daraja = DarajaAPI()
                response = daraja.stk_push(
                    phone_number=data['phone_number'],
                    amount=data['amount'],
                    account_reference=data['account_reference'],
                    transaction_desc=data['transaction_desc']
                )

                checkout_request_id = response.get('CheckoutRequestID', None)
                
                user = None
                if request.user.is_authenticated:
                    try:
                        user = AppUser.objects.get(user=request.user)
                    except ObjectDoesNotExist:
                        return Response(
                            {"error": "Authenticated user not found in AppUser"},
                            status=status.HTTP_400_BAD_REQUEST
                        )
                
                if checkout_request_id:
                    payment = PaymentDetails.objects.create(
                        phone_number=data['phone_number'],
                        amount=data['amount'],
                        account_reference=data['account_reference'],
                        transaction_desc=data['transaction_desc'],
                        mpesa_checkout_id=checkout_request_id,
                        quantity=1,
                        type='payment',
                        condition='New',
                        price=data['amount'],
                    )
                    if user:
                        if user.role == 'trader':
                            payment.trader = user
                        elif user.role == 'upcycler':
                            payment.upcycler = user
                        payment.save()

                return Response(response, status=status.HTTP_200_OK)
            
            except APIException as e:
                return Response(
                    {"error": str(e)},
                    status=status.HTTP_400_BAD_REQUEST
                )
            except Exception as e:
                return Response(
                    {"error": f"Unexpected error: {str(e)}"},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RegisterView(generics.CreateAPIView):
    serializer_class = RegistrationSerializer
    permission_classes = [AllowAny]

    def notify_receiver(self, receiver_phone: str, amount: str, order_id: str, status: str):
        message = f"Payment of {amount} KSH for order {order_id} {status}."
        logger.info(f"Notification to receiver {receiver_phone}: {message}")
        africastalking.initialize(
                username=config('AFRICASTALKING_USERNAME'),
                api_key=config('AFRICASTALKING_API_KEY')
            )
        sms = africastalking.SMS
        try:
            response = sms.send(message, [receiver_phone])
            logger.info(f"SMS sent to {receiver_phone}: {response}")
        except Exception as e:
                logger.error(f"Failed to send SMS to {receiver_phone}: {str(e)}")




@api_view(['POST'])
def daraja_callback(request): 
    callback_data = request.data
    print("Daraja Callback Data:", callback_data)

    try:
        stk_callback = callback_data['Body']['stkCallback']
        checkout_request_id = stk_callback['CheckoutRequestID']
        result_code = stk_callback['ResultCode']
        result_desc = stk_callback['ResultDesc']
        payment = PaymentDetails.objects.get(mpesa_checkout_id=checkout_request_id)

        payment.result_code = str(result_code)
        payment.result_description = result_desc

        if result_code == 0:
            items = stk_callback.get('CallbackMetadata', {}).get('Item', [])
            item_dict = {item['Name']: item['Value'] for item in items}

            payment.mpesa_receipt_number = item_dict.get('MpesaReceiptNumber')
            trans_date_str = str(item_dict.get('TransactionDate'))
            trans_date = datetime.datetime.strptime(trans_date_str, '%Y%m%d%H%M%S')
            payment.transaction_date = timezone.make_aware(trans_date, timezone.get_current_timezone())

            payment.amount_from_callback = item_dict.get('Amount')
            payment.phone_number_from_callback = item_dict.get('PhoneNumber')
            payment.payment_status = 'Completed'
        else:
            payment.payment_status = 'Failed'

        payment.save()

    except PaymentDetails.DoesNotExist:
        print(f"Payment with CheckoutRequestID {checkout_request_id} not found.")
    except Exception as e:
        print(f"Error processing Daraja callback: {e}")
    return Response({"ResultCode": 0, "ResultDesc": "Accepted"})









