#Para poder usar comandos relativos a la base de datos
import sqlite3

conexion = sqlite3.connect("Biblioteca.db")

cursor = conexion.cursor()

#Crear las tablas

cursor.execute('''
               CREATE TABLE IF NOT EXISTS Libros(
               id_libro INTEGER PRIMARY KEY AUTOINCREMENT,
               titulo TEXT,
               autor TEXT,
               anio_publicacion INTEGER,
               cantidad_disponible INTEGER
               )
               ''')

cursor.execute('''
               CREATE TABLE IF NOT EXISTS Lectores(
               id_lector INTEGER PRIMARY KEY AUTOINCREMENT,
               nombre TEXT,
               correo TEXT
               )
               ''')

cursor.execute('''
               CREATE TABLE IF NOT EXISTS Prestamos(
               id_prestamo INTEGER PRIMARY KEY AUTOINCREMENT,
               id_lector INTEGER,
               id_libro INTEGER,
               fecha_prestamo DATE,
               fecha_devolucion DATE,
               FOREIGN KEY(id_lector) REFERENCES Lectores(id_lector)
               FOREIGN KEY(id_libro) REFERENCES Libros(id_libro)
               )
               ''')

class Libros:
    def __init__(self, titulo, autor, anio_publicacion, cantidad_disponible):
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion
        self.cantidad_disponible = cantidad_disponible
    
    def registraLibro():
        try:
            cursor.execute("")
        except Exception as e:
            print(f"Error: {e}")   

class Lectores:
    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo

class Prestamos:
    def __init__(self, id_lector, id_libro, fecha_prestamo, fecha_devolucion):
        self.id_lector = id_lector
        self.id_libro = id_libro
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion

def menu():
    while(True):
        print("OPCIONES")
        print("1. Registrar un libro")
        print("2. Registrar un lector")
        print("3. Registrar un préstamo")
        print("4. Listar préstamos activos")
        print("5. Devolver un libro")
        print("6. Salir del sistema")
        opcion = int(input("Dime la opcion que quieres: "))

        match(opcion):
            case 1:


