# Diseña un sistema para gestionar reservas en un hotel. Hay tres tipos de habitaciones: 
# Individual, Doble y Suite. Cada tipo tiene un precio base y características específicas: 
#   Las Individuales tienen un precio base de 50 € por noche. 
#   Las Dobles tienen un precio base de 75 € por noche y permiten un suplemento de 
# desayuno (+10 €). 
#   Las Suites tienen un precio base de 150 € por noche y permiten un descuento del 
# 10% para estancias largas (más de 3 noches). 
# Enunciado: 
# 1.  Crea una clase base Habitacion con un método calcular_precio(noches). 
# 2.  Implementa clases derivadas para cada tipo de habitación. 
# 3.  Crea una lista de habitaciones y calcula el precio total para varias reservas.

#! 1. Crear la clase Habitacion-------------------------------------------------
class Habitacion():

    def __init__(self,precio_base:float = 0.00):
        self.__precio_base = precio_base

    @property
    def precio_base(self):
        return self.__precio_base
    
    @precio_base.setter
    def precio_base(self,valor):

        if valor < 0:
            raise ValueError ("El precio no puede ser menor a 0.")

        self.__precio_base = valor

    def precio_total(self,noches:int):
        return (self.precio_base * noches)




#! 2. Clases Derivadas-------------------------------------------
class Individuales(Habitacion):

    # Asi le digo que el precio sea 50 siempre
    def __init__(self):
        super().__init__(50.00)

class Dobles(Habitacion):

    def __init__(self,suplemento:bool = False):
        super().__init__(75.00)
        self.__suplemento = suplemento

    @property
    def suplemento(self):
        return self.__suplemento #Con el property obtienes el suplemento como atributo en lugar de como metodo. Aquí esto es util porque ha puesto el suplemento como privado y esta es una forma de acceder
    
    @suplemento.setter
    def suplemento(self,valor):
        self.suplemento = valor

    # Sobreescribimos el metodo precio total
    def precio_total(self, noches: int):
        if self.suplemento:
            return super().precio_total(noches) + (10 * noches)
        else :
            return super().precio_total(noches)

class Suites(Habitacion):

    def __init__(self):
        super().__init__(150.00) 
    
    # Sobreescribimos el metodo precio total
    def precio_total(self, noches: int):
        if noches<3:
            return super().precio_total(noches)
        else :
            return super().precio_total(noches) - (super().precio_total(noches) * 0.1)
    
        
        
def main():
    try:
    
        habitaciones = [
            Individuales(),
            Dobles(True),
            Suites()
        ]

        for habitacion in habitaciones:
            print(f"El precio total de 5 noches en {type(habitacion).__name__} es: {habitacion.precio_total(5)}")

    except ValueError as e:
        print(f"Error al calcular el precio: {e}")


# Ejecutamos el main
if __name__ == "__main__":
    main()