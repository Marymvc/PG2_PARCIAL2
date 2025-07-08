class ConoBase:
    def __init__(self):
        self.ingredientes = []
        self.precio = 0

    def inicializar(self):
        raise NotImplementedError()

    def obtener_ingredientes_base(self):
        return self.ingredientes

    def precio_base(self):
        return self.precio


class Carnivoro(ConoBase):
    def inicializar(self):
        self.ingredientes = ["carne mechada", "queso"]
        self.precio = 20


class Vegetariano(ConoBase):
    def inicializar(self):
        self.ingredientes = ["vegetales grillados", "queso light"]
        self.precio = 18


class Saludable(ConoBase):
    def inicializar(self):
        self.ingredientes = ["pollo al vapor", "ensalada fresca"]
        self.precio = 22
