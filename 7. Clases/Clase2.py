#1. Crea  una  clase  Persona  para  guardar  nombre,  dirección  y  teléfono  de  una 
#persona. 

# 2. Crea un programa que utilice la clase Persona para almacenar un diccionario de 
# contactos. El diccionario será un conjunto de datos donde la clave de cada entrada 
# es el nombre de la persona (en mayúsculas) y el valor es un objeto de la clase 
# Persona que guarda el nombre, dirección y teléfono. 

class Persona: 
    def __init__(self, nombre, direccion, telefono):#Contructor de la clase
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
    
    def __str__(self):#Para definir cómo se muestra un objeto en una cadena de texto
        return f"Nombre: {self.nombre}, Dirección: {self.direccion}, Teléfono: {self.telefono}"


contactos = {}

def mostrarContactos():
    for contacto in contactos.values():
        print(contacto)

def agregarContacto():#Función para agregar el contacto usando clases
    nombre = input("Di el nombre: ")
    direccion = input("Di la direccion: ")
    telefono = int(input("Dime el teléfono: "))

    nombreMayus = nombre.upper()
    contacto = Persona(nombre, direccion, telefono)
    contactos[nombreMayus] = contacto

def modificarContacto():
    nombre = input("Di el contacto que quieras modificar: ")
    nombreMayus = nombre.upper()
 
    if nombreMayus in contactos:
        direccion = input("Introduce la nueva dirección: ")
        telefono = int(input("Introduce el nuevo teléfono: "))

        contacto = Persona(nombre, direccion, telefono)
        contactos[nombreMayus] = contacto
    else:
        print("Contacto no encontrado")

def buscarNumTlf():
    telefono = int(input("Dime el número que desees buscar: "))
    encontrado = False
    for contacto in contactos.values(): #Aquí usamos el bucle for porque no es una clave dentro del diccionario, sino un valor dentro de la clave. Por eso tenemos que recorrer los valores
        if contacto.telefono == telefono:
            print(f"El contacto que buscas es: Nombre: {contacto.nombre}, Teléfono: {contacto.telefono}, Dirección: {contacto.direccion}")
            encontrado = True
    if not encontrado:
        print("El contacto no existe")


def eliminarContacto():
    nombre = input("Dime el nombre del contacto que quieres eliminar: ")
    if nombre in contactos:#Aquí no hace falta usar un bucle for. Estamos buscando la clave
        del contactos[nombre]
    else:
        print("Ese contacto no existe")


def menu():    
    while (True):
        print("a. Listado de contactos")
        print("b. Añadir un nuevo contacto")
        print("c. Modificar un contacto")
        print("d. Buscar un número de teléfono")
        print("e. Eliminar un contacto")
        print("f. Salir")

        opcion = input("Dime la opción: ")
        match opcion.lower():
            case "a":
                mostrarContactos()
            case "b":
                agregarContacto()
            case "c":
                modificarContacto()
            case "d":
                buscarNumTlf()
            case "e":
                eliminarContacto()
            case "f":
                print("Saliendo...")
            case default:
                print("Opción no válida")

menu()
                