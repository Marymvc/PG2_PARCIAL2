from rest_framework import serializers
from api_conos.models import PedidoCono
from api_conos.factory import ConoFactory
from api_conos.builder import ConoPersonalizadoBuilder, ConoDirector
from api_patrones.logger import Logger

class PedidoConoSerializer(serializers.ModelSerializer):
    precio_total = serializers.SerializerMethodField()
    ingredientes_finales = serializers.SerializerMethodField()

    class Meta:
        model = PedidoCono
        fields = [
            "id",
            "cliente",
            "variante",
            "toppings",
            "tamanio_cono",
            "fecha_pedido",
            "precio_total",
            "ingredientes_finales",
        ]

    def get_precio_total(self, obj):
        base = ConoFactory.obtener_base(obj.variante)
        builder = ConoPersonalizadoBuilder(base)
        director = ConoDirector(builder)
        director.construir(obj.toppings, obj.tamanio_cono)
        return builder.obtener_precio()

    def get_ingredientes_finales(self, obj):
        base = ConoFactory.obtener_base(obj.variante)
        builder = ConoPersonalizadoBuilder(base)
        director = ConoDirector(builder)
        director.construir(obj.toppings, obj.tamanio_cono)
        return builder.obtener_ingredientes_finales()

