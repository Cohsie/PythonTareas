class Vehiculo:
    def __init__(self, identificador, modelo, estado="disponible"):
        self.identificador = identificador
        self.modelo = modelo
        self.estado = estado
    
    def cambiar_estado(self):
        if self.estado == "disponible":
            self.estado = "en servicio"
        else:
            self.estado = "disponible"
    
    def mostrar_info(self):
        return f"ID: {self.identificador}, Modelo: {self.modelo}, Estado: {self.estado}"

class Auto(Vehiculo):
    def __init__(self, identificador, modelo, num_asientos, estado="disponible"):
        if num_asientos <= 1:
            raise ValueError("El número de asientos debe ser mayor a 1.")
        super().__init__(identificador, modelo, estado)
        self.num_asientos = num_asientos
    
    def mostrar_info(self):
        return f"{super().mostrar_info()}, Asientos: {self.num_asientos}"

class Camion(Vehiculo):
    def __init__(self, identificador, modelo, capacidad_carga, estado="disponible"):
        if capacidad_carga <= 0:
            raise ValueError("La capacidad máxima de carga debe ser mayor a 0.")
        super().__init__(identificador, modelo, estado)
        self.capacidad_carga = capacidad_carga
    
    def mostrar_info(self):
        return f"{super().mostrar_info()}, Capacidad de carga: {self.capacidad_carga} kg"

class GestionFlota:
    def __init__(self):
        self.vehiculos = {}
    
    def registrar_vehiculo(self, vehiculo):
        if vehiculo.identificador in self.vehiculos:
            print(f"Vehículo con ID {vehiculo.identificador} ya registrado.")
        else:
            self.vehiculos[vehiculo.identificador] = vehiculo
            print(f"Vehículo {vehiculo.modelo} registrado con éxito.")
    
    def consultar_vehiculo(self, identificador):
        vehiculo = self.vehiculos.get(identificador)
        if vehiculo:
            print(vehiculo.mostrar_info())
        else:
            print(f"Vehículo con ID {identificador} no encontrado.")
    
    def listar_vehiculos_disponibles(self):
        disponibles = []
        for vehiculo in self.vehiculos.values():
            if vehiculo.estado == "disponible":
                disponibles.append(vehiculo.mostrar_info())
        
        if disponibles:
            print("\nVehículos disponibles:")
            for vehiculo in disponibles:
                print(vehiculo)
        else:
            print("No hay vehículos disponibles.")
    
    def cambiar_estado_vehiculo(self, identificador):
        vehiculo = self.vehiculos.get(identificador)
        if vehiculo:
            vehiculo.cambiar_estado()
            print(f"Estado del vehículo con ID {identificador} cambiado a {vehiculo.estado}.")
        else:
            print(f"Vehículo con ID {identificador} no encontrado.")
    
    def eliminar_vehiculo(self, identificador):
        if identificador in self.vehiculos:
            del self.vehiculos[identificador]
            print(f"Vehículo con ID {identificador} eliminado.")
        else:
            print(f"Vehículo con ID {identificador} no encontrado.")

def main():
    gestion = GestionFlota()

    # Registrar vehículos
    auto1 = Auto("A123", "Toyota Corolla", 5)
    auto2 = Auto("B456", "Honda Civic", 4)
    camion1 = Camion("C789", "Volvo FH", 15000)

    gestion.registrar_vehiculo(auto1)
    gestion.registrar_vehiculo(auto2)
    gestion.registrar_vehiculo(camion1)

    # Consultar vehículos
    gestion.consultar_vehiculo("A123")
    gestion.consultar_vehiculo("B456")
    gestion.consultar_vehiculo("C789")

    # Listar vehículos disponibles
    gestion.listar_vehiculos_disponibles()

    # Cambiar estado de un vehículo
    gestion.cambiar_estado_vehiculo("A123")
    
    # Listar vehículos disponibles después del cambio
    gestion.listar_vehiculos_disponibles()

    # Eliminar un vehículo
    gestion.eliminar_vehiculo("B456")
    gestion.listar_vehiculos_disponibles()

if __name__ == "__main__":
    main()
