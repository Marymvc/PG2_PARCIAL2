from django.contrib import admin
from .models import PedidoCono

@admin.register(PedidoCono)
class PedidoConoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'variante', 'tamanio_cono', 'fecha_pedido', 'toppings_display')
    list_filter = ('variante', 'tamanio_cono', 'fecha_pedido')
    search_fields = ('cliente', 'variante')

    def toppings_display(self, obj):
        return ", ".join(obj.toppings) if obj.toppings else "Ninguno"
    toppings_display.short_description = "Toppings"


