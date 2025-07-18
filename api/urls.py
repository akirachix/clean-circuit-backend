from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserViewSet, UpcyclerClothesRequestViewSet,
    PaymentViewSet, UpcycledProductViewSet,
    MaterialViewSet, MaterialCatalogueViewSet
)
router = DefaultRouter()

router.register(r'users', UserViewSet, basename='users')
router.register(r'upcycler-requests', UpcyclerClothesRequestViewSet, basename='upcycler-requests')
router.register(r'payments', PaymentViewSet, basename='payments')
router.register(r'upcycled-products', UpcycledProductViewSet, basename='upcycled-products')
router.register(r'materials', MaterialViewSet, basename='materials')
router.register(r'catalogue', MaterialCatalogueViewSet, basename='catalogue')

urlpatterns = [
    path('', include(router.urls)),
]
