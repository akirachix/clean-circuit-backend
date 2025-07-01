from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (UpcycledProductViewSet,UserViewSet)


router = DefaultRouter()
router.register(r'upcycled-products', UpcycledProductViewSet, basename='upcycled-products')
router.register(r'user', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
]   