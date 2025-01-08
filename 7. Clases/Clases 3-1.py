class Productos:
    def __init__(self, nombre, precio, descuento):
        self.nombre = nombre
        self.precio = precio
        self.descuento = descuento

class Electronicos(Productos):
    def __init__(self, nombre, precio, descuento):
        super().__init__(nombre, precio, descuento)

    def precioFinal(self):
        if self.descuento > 10:
            self.descuento = 10

        precioDescuento = self.precio * (1 - self.descuento/ 100)#Aquí se aplica el descuento, el precio multiplicado lo aplica
        return round(precioDescuento, 2)#round se utiliza para redondear. EN este caso a 2 decimales
    
class Ropa(Productos):
    def __init__(self, nombre, precio, descuento):
        super().__init__(nombre, precio, descuento)
    
    def precioFinal(self):
        if self.descuento > 20:
            self.descuento = 20
        precioDescuento = self.precio * (1-self.descuento/100)
        return round(precioDescuento, 2)

class Comida(Productos):
    def __init__(self, nombre, precio, descuento):
        super().__init__(nombre, precio, descuento)

    def precioFinal(self):
        return round(self.precio, 2)
    
#Crear una lista con productos
product = [
    Electronicos("PS4", 200, 10),
    Comida("Campero de Atún", 3.50, 0),
    Ropa("Chaqueta", 20, 30)
]

for p in product:
    print(f"Nombre: {p.nombre}, Precio final: {p.precioFinal()}")

