class ConoPersonalizadoBuilder:
    def __init__(self, base_cono):
        self.base = base_cono
        self.precio = base_cono.precio_base()
        self.ingredientes = list(base_cono.obtener_ingredientes_base())

    def agregar_topping(self, topping):
        precios = {
            "queso_extra": 1.5,
            "papas_al_hilo": 2,
            "salchicha_extra": 2.5,
            "salsa_bbq": 1,
            "aguacate": 3,
        }
        if topping not in precios:
            raise ValueError(f"Topping '{topping}' no válido.")
        self.ingredientes.append(topping)
        self.precio += precios[topping]

    def ajustar_tamanio(self, tamanio):
        if tamanio == "mediano":
            self.precio *= 1.2
        elif tamanio == "grande":
            self.precio *= 1.5

    def obtener_precio(self):
        return round(self.precio, 2)

    def obtener_ingredientes_finales(self):
        return self.ingredientes


class ConoDirector:
    def __init__(self, builder):
        self.builder = builder

    def construir(self, toppings, tamanio):
        for t in toppings:
            self.builder.agregar_topping(t)
        self.builder.ajustar_tamanio(tamanio)
