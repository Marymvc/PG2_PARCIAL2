# PG2_PARCIAL2
## DATOS PERSONALES
Nombre: Mary Magali Villca Cruz
Curso: Segundo anio
Materia: Programacion 2
Fecha: 8 de julio de 2025
## DESCRIPCION DE PATRONES
``` python
def get_precio_total(self, obj):
    base = ConoFactory.obtener_base(obj.variante)  # Factory
    builder = ConoPersonalizadoBuilder(base)       # Builder
    director = ConoDirector(builder)
    director.construir(obj.toppings, obj.tamanio_cono)

    Logger().registrar(f"Se registró el cálculo del precio del cono {obj.id}")  # Singleton

    return builder.obtener_precio()
```

## 1. 🏭 Factory

    Código aplicado:

    base = ConoFactory.obtener_base(obj.variante)

    Descripción:
    El patrón Factory selecciona y devuelve una instancia de una clase hija concreta (Carnivoro, Vegetariano, Saludable) según el valor de variante.

    Ventaja:
    Encapsula la lógica de creación de objetos. Permite agregar más variantes fácilmente sin modificar el método.

## 2. 🧱 Builder

    Código aplicado:

    builder = ConoPersonalizadoBuilder(base)
    director = ConoDirector(builder)
    director.construir(obj.toppings, obj.tamanio_cono)

    Descripción:
    El patrón Builder separa el proceso de construcción del objeto ConoPersonalizado, agregando toppings y ajustando el tamaño.

    Ventaja:
    Flexibilidad para construir conos personalizados sin modificar la lógica principal del programa.

## 3. 👤 Singleton

    Código aplicado:

Logger().registrar(f"Se registró el cálculo del precio del cono {obj.id}")

Descripción:
El patrón Singleton asegura que Logger tenga una única instancia compartida en toda la aplicación para registrar eventos.

Ventaja:
Evita múltiples instancias de logger, manteniendo centralizado el historial de acciones del sistema.

## Administrador de Django y de la lista de registros en el endpoint de API REST

![alt text](<VALIDACION ADMIN.png>)
![alt text](<VALIDACION API.png>)
