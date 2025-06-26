from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ( UserViewSet,MaterialViewSet,
)

router = DefaultRouter()
router.register(r'user', UserViewSet, basename="user")
router.register(r'materials', MaterialViewSet, basename="materials")


urlpatterns = [
    path("", include(router.urls)),
]