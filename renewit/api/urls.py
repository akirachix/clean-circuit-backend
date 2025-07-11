from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import MaterialViewSet


router = DefaultRouter()
router.register(r'materials', MaterialViewSet, basename="materials")

from .views import MaterialCatalogueViewSet


router = DefaultRouter()
router.register(r'catalogue',MaterialCatalogueViewSet, basename='catalogue')

from .views import ( UserViewSet, UpcyclerClothesRequestViewSet,
)

router = DefaultRouter()
router.register(r'user', UserViewSet, basename="user")
router.register(r'clothes-requests', UpcyclerClothesRequestViewSet, basename="clothes-requests")





urlpatterns = [
    path("", include(router.urls)),
]