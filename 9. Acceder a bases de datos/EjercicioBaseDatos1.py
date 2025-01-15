#Conexión con base de datos
import sqlite3

conn = sqlite3.connect('Tienda.db')

cursor = conn.cursor()

#Crear tabla
cursor.execute('''
               CREATE TABLE IF NOT EXISTS Productos(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT,
                precio DECIMAL,
                stock INT
                )
               ''')

#Creación de clases
class Productos:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

class Tienda:
    def __init__(self, db_nombre="tienda.db"):
        self.db_nombre = db_nombre
        self.productos = {}
        self._initialite_database()

    def addProducto(self, Productos):
        if Productos.nombre in self.productos:
            print("Ese producto ya existe")
        else:
            self.productos[Productos.nombre] = Productos
            print(f"Se ha agregago {Productos.nombre} a la tienda")

    def eliminarProducto(self):
        product = input("Dime el nombre de un producto para borrarlo: ")

        if product in self.productos:
            valor_eliminado = self.productos.pop(product)
            print(f"{valor_eliminado} eliminado")
        else:
            print("Ese producto no existe")

    def listarProductos(self):
        with sqlite3.connect(self.db_nombre) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, nombre, precio, stock FROM productos")
            productos = cursor.fetchall()
            print("Lista de productos que hay en la tienda: ")
            for prod in productos:
                print(prod)

    

