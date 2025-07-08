from api_conos.models import PedidoCono
from api_conos.serializers import PedidoConoSerializer

from django.shortcuts import render

# Create your views here.

# Python native imports
from datetime import timedelta

# External imports
from rest_framework import viewsets
from django.utils import timezone as tz

# Local imports
from django.conf import settings

class PedidoConoViewSet(viewsets.ModelViewSet):
    queryset = PedidoCono.objects.all().order_by("-fecha_pedido")
    serializer_class = PedidoConoSerializer
