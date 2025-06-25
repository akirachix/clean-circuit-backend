from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ( TraderViewSet,MaterialViewSet,
)

router = DefaultRouter()
router.register(r'traders', TraderViewSet, basename="traders")
router.register(r'materials', MaterialViewSet, basename="materials")


urlpatterns = [
    path("", include(router.urls)),
]