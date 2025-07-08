# PG2_PARCIAL2
## DATOS PERSONALES
Nombre: Mary Magali Villca Cruz
Curso: Segundo anio
Materia: Programacion 2
Fecha: 8 de julio de 2025
## DESCRIPCION DE PATRONES
``` python
def get_precio_total(self, obj):
    # Patrón Factory
    cafe = CafeFactory.obtener_base(obj.tipo_base)

    # Patrón Builder
    builder = CafePersonalizadoBuilder(cafe)
    director = CafeDirector(builder)
    director.construir(obj.ingredientes, obj.tamanio)

    # Patrón Singleton
    Logger().registrar(f"Se registró el calculo del precio para el pedido {obj.id}")
    print(Logger().obtener_logs())

    return builder.obtener_precio()
```

## 1. 🏭 Factory — CafeFactory.obtener_base(obj.tipo_base)
Propósito del patrón: Encapsular la creación de objetos, evitando el uso directo de Espresso(), Latte(), etc.

Aplicación aquí:
La línea:

cafe = CafeFactory.obtener_base(obj.tipo_base)
decide dinámicamente qué clase concreta de café (por ejemplo Espresso, Latte, Americano) instanciar según el tipo (tipo_base).
Esto permite aislar la lógica de instanciación y facilita añadir nuevos tipos sin modificar este método.

## 2. 🧱 Builder — CafePersonalizadoBuilder y CafeDirector
Propósito del patrón: Separar la construcción de un objeto complejo de su representación.

Aplicación aquí:
Se usa un builder para armar el café personalizado paso a paso (ingredientes + tamaño), y un director que controla el orden y lógica de construcción:

builder = CafePersonalizadoBuilder(cafe)
director = CafeDirector(builder)
director.construir(obj.ingredientes, obj.tamanio)
Esto permite construir cafés personalizados con distintas combinaciones sin alterar la lógica central del objeto.

## 3. 👤 Singleton — Logger
Propósito del patrón: Asegurarse de que una clase tenga solo una instancia global, útil para logging, configuraciones, etc.

Aplicación aquí:

Logger().registrar(f"...")
La clase Logger tiene una única instancia compartida para registrar logs. Esto asegura que todos los eventos se registren en un solo lugar sin importar cuántas veces se llame Logger().


## Administrador de Django y de la lista de registros en el endpoint de API REST

![alt text](<VALIDACION ADMIN.png>)
![alt text](<VALIDACION API.png>)
