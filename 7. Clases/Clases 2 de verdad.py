
#Ejercicio 1
class Persona:
    def __init__(self, nombre, apellidos, DNI, edad):#Constructor
        self.nombre = nombre
        self.apellidos = apellidos
        self.DNI = DNI
        self.edad = edad

    def mayorDeEdad(self):
        if self.edad >=18:
            print(f"{self.nombre}, es mayor de edad")

    def get_nombre(self):
        return self.nombre

    def get_apellidos(self):
        return self.apellidos
    
    def get_DNI(self):
        return self.DNI

    def get_edad(self):
        return self.edad



#Ejercicio 2
class Cuenta:
    def __init__(self, titular, cantidad):
        self.titular = titular
        self.cantidad = cantidad

    def mostrar(self):
        print(f"Titular: {self.titular.get_nombre()} {self.titular.get_apellidos()}, DNI: {self.titular.get_DNI()}, Edad: {self.titular.get_edad()}, Cantidad: {self.cantidad} ", end="")

    def ingresar(self):
        ingreso = float(input("Cuanto quieres ingresar?: "))
        self.cantidad = self.cantidad + ingreso
        print("Se han ingresado ", ingreso, " €. Ahora tu cuenta tiene ", self.cantidad, " €")

    def retirar(self):
        retiro = float(input("Cuanto quieres retirar?: "))
        if retiro <= self.cantidad:
            self.cantidad = self.cantidad - retiro
            print("Se han retirado ", retiro, " €. Ahora tu cuenta tiene ", self.cantidad, " €")
        else:
            print("No hay saldo suficiente")

#Ejercicio 3
class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad, bonificacion):
        super().__init__(titular, cantidad)
        self.bonificacion = bonificacion        
    def mostrar(self):
        super().mostrar()
        print(f"Bonificacion: {self.bonificacion}")


def main():#Crear cuenta
    print("==Sistema de creación de cuentas del banco==")
    nombre = input("Introduce tu nombre: ")
    apellido = input("Introduce tu apellido: ")
    DNI = int(input("Introduce tu DNI: "))
    edad = int(input("Introduce tu edad: "))
    while True:
        if edad >= 0:
            break
        else:
            print("No puedes poner una edad negativa")

    cantidad = int(input("Introduce la cantidad de tu cuenta: "))
    while True:
        if cantidad >= 0:
            break
        else:
            print("Introduce una cantidad que no sea negativa")
    

    titular = Persona(nombre, apellido, DNI, edad)

    tipo_cuenta = input("Selecciona el tipo de cuenta que quieres (1 para cuanta normal y 2 para cuentaJoven): ")
    while True:
        if tipo_cuenta == "1":
            cuenta = Cuenta(titular, cantidad)
            cuenta.mostrar()
        elif tipo_cuenta == "2":
            if edad < 25:
                bonificacion = int(input("Dime la bonificación de tu cuenta: "))
                cuenta = CuentaJoven(titular, cantidad, bonificacion)
                cuenta.mostrar()
                break
            else:
                print("Edad no válida para esta cuenta")
                break
        else:
            print("Introduce un tipo de cuenta válido (1 o 2)")
            break

main()
