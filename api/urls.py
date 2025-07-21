from django.urls import path, include
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.routers import DefaultRouter


from .views import (
    AppUserViewSet, 
    UpcyclerClothesRequestViewSet,
    PaymentViewSet,
    UpcycledProductViewSet,
    MaterialViewSet,
    MaterialCatalogueViewSet,
    STKPushView,
    RegisterView,
    daraja_callback
)

router = DefaultRouter()
router.register(r'users', AppUserViewSet)
router.register(r'upcycler-requests', UpcyclerClothesRequestViewSet)
router.register(r'payments', PaymentViewSet)
router.register(r'upcycled-products', UpcycledProductViewSet)
router.register(r'materials', MaterialViewSet)
router.register(r'catalogue', MaterialCatalogueViewSet)


@api_view(['GET'])
@permission_classes([AllowAny])
def custom_api_root(request, format=None):
    """
    Public API root endpoint, showing all API endpoints as absolute URLs.
    """
    return Response({
        "users": request.build_absolute_uri('users/'),
        "upcycler-requests": request.build_absolute_uri('upcycler-requests/'),
        "payments": request.build_absolute_uri('payments/'),
        "upcycled-products": request.build_absolute_uri('upcycled-products/'),
        "materials": request.build_absolute_uri('materials/'),
        "catalogue": request.build_absolute_uri('catalogue/'),
    })

urlpatterns = [
    path('', custom_api_root), 
    path("", include(router.urls)),
    path('login/', obtain_auth_token), 
    path('register/', RegisterView.as_view(), name='register'), 
    path('daraja/stk-push/', STKPushView.as_view(), name='daraja-stk-push'),
    path('daraja/callback/', daraja_callback, name='daraja-callback'),
  
]



  