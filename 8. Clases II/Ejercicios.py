'''1. Crea una clase Persona para guardar nombre, apellidos, DNI y edad de una 
persona.  
a. Define un constructor, donde se puedan indicar los datos iniciales (pueden 
estar vacíos). 
b. Para cada atributo define sus correspondientes setter (para poder validar el 
valor de entrada: nombre, apellidos y DNI no pueden ser cadenas vacías y 
se guardará en mayúsculas. Edad debe ser un valor entero positivo). 
c. Para cada atributo define sus correspondientes getter. 
d. Añade el método mostrar(), que muestra los datos de la persona (nombre, 
apellidos, DNI edad). 
e. Añade el método mayorDeEdad(), que indica si la persona es mayor de 
edad o no. '''

# Vamos a crear la clase Persona
class Persona():

    # Ahora el contructor, como dice que pueden estar vacios les doy valores por defectos vacios
    def __init__(self,nombre='',apellidos='',DNI='',edad:int=''):
        self.nombre = nombre
        self.apellidos = apellidos
        self.DNI = DNI
        self.edad = edad

    #C. Esto serian como los getters
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def apellidos(self):
        return self._apellidos
    
    @property
    def DNI(self):
        return self._DNI
    
    @property
    def edad(self):
        return self._edad

    #B. Vamos a crear los setters, nombre, dni y apellidos no pueden ser cadenas vacias y lo vamos a guardar en mayusculas, edad debe ser si o si un valor entero positivo 
    @nombre.setter
    def nombre(self,valor):

        # Lo que hace strip es quitar los espacios en blanco al principio y al final
        # Si strip devuelve la cadena vacia, dentro de python se toma como un false en expresion logica, por lo que si pongo if not es como decir si es false
        if not str(valor).strip():
            raise ValueError("El nombre no puede ser una cadena vacía.")
        
        self._nombre = valor.upper()

    @apellidos.setter
    def apellidos(self,valor):

        if not valor.strip():
            raise ValueError("El apellido no puede ser una cadena vacia.")
        
        self._apellidos = valor.upper()
        
    @DNI.setter
    def DNI(self,valor):

        if not valor.strip():
            raise ValueError("El DNI no puede ser una cadena vacia.")
        
        self._DNI = valor.upper()

    @edad.setter
    def edad(self, valor):

        if valor < 0:
            raise ValueError("La edad debe ser un número entero positivo.")
        
        self._edad = valor


    #D. Ahora vamos a hacer el metodo mostrar()
    def mostrar(self):
        return f'Nombre de la persona: {self.nombre}, Apellidos: {self.apellidos}, su DNI es: {self.DNI}, y tiene: {self.edad} años.'
    
    # E.Ahora el metodo mayorDeEdad()
    def mayorDeEdad(self):
        if self.edad < 18:
            print(f'{self.nombre} es menor de edad.')
        elif self.edad >=18:
            print(f'{self.nombre} es mayor de edad.')



# 2. Creamos la clase Cuenta
class Cuenta:

    # a. El contructor titular tiene que existir si o si
    def __init__(self,titular:Persona,cantidad:float=0):

        self.__titular = titular
        self.__cantidad = cantidad

    # b. Esto serian como los getters y setters teniendo en cuanta que hay que hacer ingreso y retirada
    @property
    def titular(self):
        return self.__titular
    
    @property
    def cantidad(self):
        return self.__cantidad
    
    # C.
    def ingresar(self, cantidad): 
        
        if cantidad < 0:
            print("La cantidad que quieres ingresar no puede ser negativa.")
        else:
            self.__cantidad += cantidad 
        
    # D.
    def retirar(self, cantidad):

        if cantidad < 0:
            print("La cantidad que quieres retirar no puede ser negativa.")
        else:
            self.__cantidad -= cantidad 
    # E.
    def mostrar(self):
        return self.__titular.mostrar() + f" Cantidad = {self.__cantidad}"
    
# 3. Crear clase CuentaJoven   
class CuentaJoven(Cuenta):

    # Las validaciones las hago en el constructor
    def __init__(self, titular: Persona, cantidad: float = 0, bonificacion: float = 0):

        if titular.edad >= 25:
            raise ValueError("El titular debe ser menor de 25 años para una Cuenta Joven.")
        if not (0 <= bonificacion <= 100):
            raise ValueError("La bonificación debe ser un valor entre 0 y 100.")
        
        super().__init__(titular, cantidad)
        self.bonificacion = bonificacion

    @property
    def bonificacion(self):
        return self.__bonificacion
    
    @bonificacion.setter
    def bonificacion(self, valor):
        if not (0 <= valor <= 100):
            raise ValueError("La bonificación debe ser un valor entre 0 y 100.")
        self.__bonificacion = valor
    
    def mostrar(self):
        return super().mostrar() + f", Bonificación = {self.bonificacion}%"



def main():

    #! Ahora vamos a probar el codigo Persona
    prueba = Persona('Juan','Carlos','79292813Z',23)
    prueba2 = Persona('Carlos','Carlos','79292813Z',17)
    prueba3= Persona('Irene','Carlos','79292813Z',18)

    # cuenta = Cuenta() 

    # print(prueba.mostrar())
    # print(prueba2.mayorDeEdad())
    # print(prueba3.mayorDeEdad())

    #! Pruebas de clase Cuenta:
    cuenta1 = Cuenta(prueba,0)
    # print(cuenta1.mostrar())

    # # Ingresamos
    # cuenta1.ingresar(1000)
    # print(cuenta1.mostrar())

    # cuenta1.retirar(500)
    # print(cuenta1.mostrar())

    # cuenta1.retirar(1500)
    # print(cuenta1.mostrar())

    # cuenta1.retirar(-1000)
    # cuenta1.ingresar(-1000)
    # print(cuenta1.mostrar())

    #!Pruba de CuentaJoven
    # Prueba con titular mayor a 25 años
    try: 
        adulto = Persona('Pedro', 'García', '87654321B', 30) 
        cuenta_joven_invalida = CuentaJoven(adulto, 500, 10) 
    except ValueError as e: 
        print(e)

    # Prueba con bonificación fuera de rango 
    try: 
        joven_invalida = Persona('María', 'López', '23456789C', 22) 
        cuenta_joven_bonificacion_invalida = CuentaJoven(joven_invalida, 500, 150) 
    except ValueError as e: 
        print(e)

main()

    
