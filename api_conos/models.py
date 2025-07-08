# api_conos/models.py

from django.db import models
from django.core.exceptions import ValidationError
from api_conos.factory import ConoFactory
from api_conos.builder import ConoPersonalizadoBuilder


class PedidoCono(models.Model):
    VARIANTES = [
        ("carnivoro", "Carnívoro"),
        ("vegetariano", "Vegetariano"),
        ("saludable", "Saludable"),
    ]

    TAMANIOS = [
        ("pequeño", "Pequeño"),
        ("mediano", "Mediano"),
        ("grande", "Grande"),
    ]

    cliente = models.CharField(max_length=100)
    variante = models.CharField(max_length=20, choices=VARIANTES)
    toppings = models.JSONField(default=list)
    tamanio_cono = models.CharField(max_length=10, choices=TAMANIOS)
    fecha_pedido = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.cliente} - {self.variante}"



