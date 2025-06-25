from trader.models import Trader, Material
from rest_framework import viewsets
from .serializers import (
    TraderSerializer, MaterialSerializer,
)
class TraderViewSet(viewsets.ModelViewSet):
    queryset = Trader.objects.all()
    serializer_class = TraderSerializer

class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
