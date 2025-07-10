from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (UpcycledProductViewSet)


router = DefaultRouter()
router.register(r'upcycled-products', UpcycledProductViewSet, basename='upcycled-products')


urlpatterns = [
    path('', include(router.urls)),
]   