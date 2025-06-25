from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ( UpcyclerViewSet, UpcyclerClothesRequestViewSet,
    UpcycledProductViewSet,TraderViewSet,MaterialViewSet,PaymentViewSet,CatalogueViewSet,
)

router = DefaultRouter()
router.register(r'upcyclers', UpcyclerViewSet, basename="upcyclers")
router.register(r'clothes-requests', UpcyclerClothesRequestViewSet, basename="clothes-requests")
router.register(r'upcycled-products', UpcycledProductViewSet, basename="upcycled-products")
router.register(r'traders', TraderViewSet, basename="traders")
router.register(r'materials', MaterialViewSet, basename="materials")
router.register(r'payments', PaymentViewSet, basename="payments")
router.register(r'catalogue',CatalogueViewSet, basename='catalogue')

urlpatterns = [
    path("", include(router.urls)),
]