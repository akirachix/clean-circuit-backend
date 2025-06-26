from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ( UpcyclerViewSet, UpcyclerClothesRequestViewSet,
)

router = DefaultRouter()
router.register(r'upcyclers', UpcyclerViewSet, basename="upcyclers")
router.register(r'clothes-requests', UpcyclerClothesRequestViewSet, basename="clothes-requests")



urlpatterns = [
    path("", include(router.urls)),
]