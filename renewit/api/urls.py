from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MaterialCatalogueViewSet


router = DefaultRouter()
router.register(r'catalogue',MaterialCatalogueViewSet, basename='catalogue')

urlpatterns = [
    path("", include(router.urls)),
]