#1. Crea  una  clase  Persona  para  guardar  nombre,  dirección  y  teléfono  de  una 
#persona. 

class Persona: 
    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono

# 2. Crea un programa que utilice la clase Persona para almacenar un diccionario de 
# contactos. El diccionario será un conjunto de datos donde la clave de cada entrada 
# es el nombre de la persona (en mayúsculas) y el valor es un objeto de la clase 
# Persona que guarda el nombre, dirección y teléfono. 

Contactos = {}

def listarContacto():# Esto es para ver
    if not Contactos:
        print("No hay contactos")
    else:
        for nombre, numero in Contactos:
            print(f"{nombre}: {numero}")

def anadirContacto():
    nombre = input("Escribe el nombre")
    direccion =  input("Escribe la dirección")
    numero = int(input("Escribe el número"))
    p1 = Persona(nombre, direccion, numero)
    Contactos[nombre] = p1

def modificarContacto():
    if not Contactos:
        r = input("Quieres escribir un nuevo contacto?")
        if r.lower() == "si":
            anadirContacto()
            print("Se ha añadido el contacto")
        else:
            print("Vale, volviendo al menú")
    else:
        nombre = input("Escribe el nombre del contacto que quieres modificar")
        if nombre in Contactos:
            newTelefono = int(input("Dime el nuevo número"))
            Contactos[nombre] = newTelefono
            print(f"{nombre} con número cambiado")
        else:
            print("Contacto no encontrado")

def buscarNumTlf():
    number = int(input("Dime a quién quieres buscar"))
    for nombre, number in Contactos:          
        if number == Contactos.items():
            print(f"{number} pertenece a {nombre}")

def eliminarContacto():
    nombre = input("Dime el contacto que deseas eliminar: ")
    if nombre in Contactos:
        del Contactos[nombre]
        print(f"Contacto {nombre} eliminado")
    

def menu():    
    print("a. Listado de contactos por orden alfabético")
    print("b. Añadir un nuevo contacto")
    print("c. Modificar un contacto")
    print("d. Buscar un número de teléfono")
    print("e. Eliminar un contacto")
    print("f. Salir")

    opcion = 0
    match opcion.lower():
        case "a":
            listarContacto()
        case "b":
            anadirContacto()
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
                