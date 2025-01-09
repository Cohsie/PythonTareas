#Conexión con base de datos
import sqlite3

conn = sqlite3.connect('Tienda.db')

conn = conn.cursor()

#Creación de clases
class Tienda:
    def __init__(self, nombre, lugar):
        self.nombre = nombre
        self.lugar = lugar

class Productos:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

#Creación de diccionario
diccionario = {}

producto1 = Productos("Bocadillo de atún", 2.50, 8)
producto2 = Productos("Yatekomo", 1.00, 12)

diccionario[1] = {"nombre":producto1.nombre,"precio":producto1.precio,"stock":producto1.stock}
diccionario[2] = {"nombre":producto2.nombre,"precio":producto2.precio,"stock":producto2.stock}

def aniadirProducto():
    id = int(input("Dime el id del producto: "))
    nombre = input("Dime el nombre del producto: ")
    precio = float(input("Dime el precio del producto: "))
    stock = int(input("Dime el stock del producto: "))

    productoA = Productos(nombre, precio, stock)

    diccionario[id] = {"nombre":productoA.nombre,"precio":productoA.precio,"stock":productoA.stock}

def menu():
    while(True):
        print("OPCIONES")
        print("1. Introducir producto")
        print("2. Ver productos")
        print("3. Eliminar producto")
        print("4. Salir")

        opcion = 0

    match opcion:
        case 1:
            aniadirProducto()




