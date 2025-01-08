#Herencia simple
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        return "Guau"
    
class Gato(Animal):
    def hacer_sonido(self):
        return "Miau"
    
perrito = Perro("Firulais")
gatito = Gato("Michi")

print(f"{perrito.nombre} dice: {perrito.hacer_sonido()}")
print(f"{gatito.nombre} dice: {gatito.hacer_sonido()}")

class Volador:
    def volar(self):
        return "Estoy volando"
    
class Pato(Animal, Volador):#Clase que hereda de Animal y de Volador
    def hacer_sonido(self):
        return "Cuac!"
    
patito = Pato("Donald")
print(f"{patito.nombre} dice: {patito.hacer_sonido()}")
print(patito.volar())


class Persona:
    def __init__(self, nombre):#Recuerda, este es el constructor
        self.nombre = nombre
    
    def saludar(self):#Y este es un método de la clase
        return f"Hola, soy {self.nombre}"
    
class Estudiante(Persona):#Clase estudiante que hereda de Persona
    def __init__(self, nombre, universidad):
        super().__init__(nombre)#Para acceder a la versión original del método
        self.universidad = universidad
    
    def saludar(self):
        return super().saludar() + f" y estudio en {self.universidad}"