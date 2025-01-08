class Habitacion:
    def __init__(self, precio):
        self.precio = precio

    def calcular_precio(self, noches):
        return self.precio * noches


class Individuales(Habitacion):
    def __init__(self):
        super().__init__(50)


class Dobles(Habitacion):
    def __init__(self):
        super().__init__(75)

    def calcular_precio(self, noches, desayuno=False):
        extra = 10 if desayuno else 0
        return (self.precio + extra) * noches


class Suite(Habitacion):
    def __init__(self):
        super().__init__(150)

    def calcular_precio(self, noches):
        descuento = 0.90 if noches > 3 else 1
        return (self.precio * noches) * descuento


def main():
    habitaciones = [
        Individuales(),
        Dobles(),
        Suite()
    ]

    noches = int(input("¿Cuántas noches desea reservar?: "))
    desayuno = input("¿Quiere desayuno para habitaciones dobles? (si/no): ").strip().lower() == "si"

    for habitacion in habitaciones:
        if isinstance(habitacion, Dobles):
            precio_total = habitacion.calcular_precio(noches, desayuno)
        else:
            precio_total = habitacion.calcular_precio(noches)

        print(f"Precio total = {precio_total} €")

main()
