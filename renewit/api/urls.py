from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (UpcycledProductViewSet,UpcyclerViewSet)


router = DefaultRouter()
router.register(r'upcycled-products', UpcycledProductViewSet, basename='upcycled-products')
router.register(r'upcycler', UpcyclerViewSet, basename='upcycler')

urlpatterns = [
    path('', include(router.urls)),
]