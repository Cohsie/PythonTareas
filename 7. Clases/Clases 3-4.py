from abc import ABC, abstractmethod

# Clase base abstracta
class Empleado(ABC):
    def __init__(self, nombre, empleado_id):
        self.nombre = nombre
        self.empleado_id = empleado_id

    @abstractmethod
    def calcular_salario(self):
        pass

    def mostrar_info(self):
        return f"ID: {self.empleado_id}, Nombre: {self.nombre}"

# Clase derivada para Empleados Asalariados
class EmpleadoAsalariado(Empleado):
    def __init__(self, nombre, empleado_id, salario_mensual):
        super().__init__(nombre, empleado_id)
        self.salario_mensual = salario_mensual

    def calcular_salario(self):
        return self.salario_mensual

    def mostrar_info(self):
        return f"{super().mostrar_info()}, Tipo: Asalariado, Salario: {self.salario_mensual}"

# Clase derivada para Empleados Por Hora
class EmpleadoPorHora(Empleado):
    def __init__(self, nombre, empleado_id, tarifa_por_hora, horas_trabajadas):
        super().__init__(nombre, empleado_id)
        self.tarifa_por_hora = tarifa_por_hora
        self.horas_trabajadas = min(horas_trabajadas, 160)  # Máximo 160 horas al mes

    def calcular_salario(self):
        return self.tarifa_por_hora * self.horas_trabajadas

    def mostrar_info(self):
        return f"{super().mostrar_info()}, Tipo: Por Hora, Horas trabajadas: {self.horas_trabajadas}, Salario: {self.calcular_salario()}"

# Clase derivada para Empleados Comisionistas
class EmpleadoComisionista(Empleado):
    def __init__(self, nombre, empleado_id, salario_base, porcentaje_comision, ventas_realizadas):
        super().__init__(nombre, empleado_id)
        self.salario_base = salario_base
        self.porcentaje_comision = porcentaje_comision
        self.ventas_realizadas = ventas_realizadas

    def calcular_salario(self):
        return self.salario_base + (self.porcentaje_comision / 100 * self.ventas_realizadas)

    def mostrar_info(self):
        return f"{super().mostrar_info()}, Tipo: Comisionista, Ventas: {self.ventas_realizadas}, Salario: {self.calcular_salario()}"

# Clase para gestionar los empleados de la empresa
class GestionEmpleados:
    def __init__(self):
        self.empleados = []

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)

    def calcular_salario_total(self):
        total = 0
        for empleado in self.empleados:
            total += empleado.calcular_salario()
        return total

    def mostrar_empleados(self):
        for empleado in self.empleados:
            print(empleado.mostrar_info())

# Programa principal
def main():
    # Crear instancia de GestionEmpleados
    gestion = GestionEmpleados()

    # Crear empleados
    asalariado1 = EmpleadoAsalariado("Juan Pérez", "A001", 2500)
    asalariado2 = EmpleadoAsalariado("Ana Gómez", "A002", 3000)
    por_hora1 = EmpleadoPorHora("Carlos Ruiz", "P001", 15, 160)
    comisionista1 = EmpleadoComisionista("Marta López", "C001", 1500, 10, 50000)

    # Agregar empleados a la gestión
    gestion.agregar_empleado(asalariado1)
    gestion.agregar_empleado(asalariado2)
    gestion.agregar_empleado(por_hora1)
    gestion.agregar_empleado(comisionista1)

    # Mostrar empleados
    print("Lista de Empleados:")
    gestion.mostrar_empleados()

    # Calcular salario total de la empresa
    total_empresa = gestion.calcular_salario_total()
    print(f"\nSalario total de la empresa: {total_empresa}")

if __name__ == "__main__":
    main()
