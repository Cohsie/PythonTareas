class Vehiculo:
    def __init__(self, modelo: str, anio: int, consumo: int):
        self.modelo = modelo
        self.anio = anio
        self.consumo = consumo 
    def calcularConsumo(self, trayecto: int):
        consumo_total = (self.consumo * trayecto)/100
        return consumo_total

class Coche(Vehiculo):
    def __init__(self, modelo: str, anio: int):
        super().__init__(modelo, anio, 5)

class Moto(Vehiculo):
    def __init__(self, modelo: str, anio: int):
        super().__init__(modelo, anio, 2)

class Camion(Vehiculo):
    def __init__(self, modelo: str, anio: int, tonelada: int):
        super().__init__(modelo, anio, 20)
        self.tonelada = tonelada
    def calcularConsumo(self, trayecto: int):
        consumo_base = super().calcularConsumo(trayecto) 
        consumo_total = consumo_base * (self.tonelada * 0.10)
        return consumo_total

    
def main ():

    Vehiculada = [
        Coche("Citroen", 2006),
        Moto("Honda", 2015),
        Camion("Renault", 2009, 4)
    ]

    trayecto = 200

    for v in Vehiculada:
        print(f"{v.modelo} ha consumido {v.calcularConsumo(trayecto)}")

main()