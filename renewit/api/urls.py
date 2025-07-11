from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ( PaymentViewSet)


from .views import (UpcycledProductViewSet)

from .views import MaterialViewSet


router = DefaultRouter()
router.register(r'materials', MaterialViewSet, basename="materials")


from .views import MaterialCatalogueViewSet


router = DefaultRouter()
router.register(r'catalogue',MaterialCatalogueViewSet, basename='catalogue')

from .views import ( UserViewSet, UpcyclerClothesRequestViewSet,
)




router = DefaultRouter()

router.register(r'payments', PaymentViewSet, basename="payments")
urlpatterns = router.urls

router.register(r'upcycled-products', UpcycledProductViewSet, basename='upcycled-products')




urlpatterns = [
    path('', include(router.urls)),
]   