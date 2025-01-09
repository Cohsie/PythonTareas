# Ejercicio 1. Creamos la clase productos Electronicos, ropa y comida

# !Crecion de producto ------------------------------------------------------------------
class Producto():
    def __init__(self,nombre:str = "Juan",precio:float=0.00,descuento:int=0,maximo = 0):

        # Aqui controlo el descuento
        if descuento > maximo:
            raise ValueError(f"El descuento no puede ser mayor a {maximo}.")

        self.__nombre = nombre
        self.__precio = precio
        self.__descuento = descuento

    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def precio(self):
        return self.__precio
    
    @property
    def descuento(self):
        return self.__descuento
    
    @nombre.setter
    def nombre(self,valor):

        if not str(valor).strip():
            raise ValueError("El nombre no puede ser una cadena vacía.")
        
        self.__nombre = valor.upper()

    @precio.setter
    def precio(self,valor):

        if valor < 0:
            raise ValueError("No puedes meter un precio negativo.")

        self.__precio = valor

    @descuento.setter
    def descuento (self,valor):

        if valor < 0:
            raise ValueError("No puedes meter un descuento negativo.")

        self.__descuento = valor
    
    def calcular_precio_final(self) -> float:
        return self.__precio - (self.__precio * (self.descuento)/100)

    def mostrar(self):

        return f" Nombre: {self.nombre} Precio: {self.precio} Descuento: {self.descuento}"

# !Creacion de clases hijas electronicos,ropa y comida----------------------------------
class Electronicos (Producto):

    def __init__(self, nombre: str = "Juan", precio: float = 0, descuento: int = 0):

        # Aqui le indico que el maximo es 10
        super().__init__(nombre, precio, descuento,10)

class Ropa (Producto):

    def __init__(self, nombre: str = "Juan", precio: float = 0, descuento: int = 0):

        # Aqui le indico que el maximo es 20
        super().__init__(nombre, precio, descuento,20)

class Comida (Producto):

    def __init__(self, nombre: str = "Juan", precio: float = 0):

        # Como no se admite descuentos, lo quitamos directamente
        super().__init__(nombre, precio,0,0)

# MAIN
def main():

    try:

        # Lista de productos
        productos = [ Electronicos("Televisor", 500.0, 10), Electronicos("Smartphone", 300.0, 5), Ropa("Camiseta", 20.0, 17), Ropa("Pantalones", 50.0, 10), Comida("Manzana", 2.0), Comida("Pan", 1.5) ]

        # Imprimimos
        for producto in productos:
            print(f"{producto.mostrar()}")
            print(f"Precio final: {producto.calcular_precio_final()} \n")


    except ValueError as e:
        print(f"Error al crear producto: {e}")

# Ejecutamos el main
if __name__ == "__main__":
    main()