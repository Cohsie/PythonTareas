# Crea un sistema para registrar vehículos en una flota de transporte. Hay tres tipos de 
# vehículos: Coche, Camión y Moto. Todos tienen un modelo, un año y un método para 
# calcular su consumo basado en las siguientes reglas: 
#   Los Coches consumen 5 litros por cada 100 km. 
#   Los Camiones consumen 20 litros por cada 100 km, pero tienen un incremento del 
# 10% por cada tonelada de carga. 
#   Las Motos consumen 3 litros por cada 100 km. 
# Enunciado: 
# 1.  Crea una clase base Vehiculo con atributos comunes y un método 
# calcular_consumo(kilometros). 
# 2.  Implementa las clases derivadas Coche, Camion y Moto con las reglas específicas. 
# 3.  Crea instancias de cada tipo de vehículo y calcula su consumo para un trayecto de 
# 200 km.

# !Clase Vehiculo---------------------------------------------------------------------
class Vehiculo():

    def __init__(self,modelo:str,anio:int,litros:int):
        self.__modelo = modelo
        self.__anio = anio
        self.__litros = litros

    @property
    def modelo(self):
        return self.__modelo
    
    @property
    def litros(self):
        return self.__litros
    
    @property
    def anio(self):
        return self.__anio
    
    @modelo.setter
    def modelo(self,valor):

        self.__modelo = valor

    @anio.setter
    def anio(self,valor):

        self.__anio = valor

    @litros.setter
    def litros(self,valor):
        self.__litros = valor

    # Funcion que calcula el consumo
    def calcular_consumo(self,kilometros):
        return(self.litros * kilometros) / 100
    
# !Clases derivadas -------------------------------------------------------------------
class Coche(Vehiculo):

    def __init__(self, modelo: str, anio: int):
        super().__init__(modelo, anio, 5)
    #Aquí no define el método consumo porque ya está definido en la clase padre
class Moto(Vehiculo):

    def __init__(self, modelo: str, anio: int):
        super().__init__(modelo, anio, 3)

class Camiones(Vehiculo):

    def __init__(self, modelo: str, anio: int, toneladas:float):
        super().__init__(modelo, anio, 20)
        self.__toneladas = toneladas

    @property
    def toneladas(self):
        return self.__toneladas
    
    @toneladas.setter
    def toneladas(self,valor):
        self.__toneladas = valor

    def calcular_consumo(self, kilometros):
        return ((self.litros + (2 * self.toneladas)) * kilometros) / 100
    

def main():
    
    coche = Coche("Toyota Corolla", 2020) 
    camion = Camiones("Volvo FH", 2018, 5)  
    moto = Moto("Yamaha YZF-R3", 2021)

    distancia = 200

    print(f"Consumo del Coche ({coche.modelo}, {coche.anio}) para {distancia} km: {coche.calcular_consumo(distancia)} litros") 
    print(f"Consumo del Camión ({camion.modelo}, {camion.anio}) para {distancia} km con 5 toneladas: {camion.calcular_consumo(distancia)} litros") 
    print(f"Consumo de la Moto ({moto.modelo}, {moto.anio}) para {distancia} km: {moto.calcular_consumo(distancia)} litros")


# Ejecutamos el main
if __name__ == "__main__":
    main()