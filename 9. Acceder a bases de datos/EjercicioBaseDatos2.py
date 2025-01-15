import sqlite3

conn = sqlite3.connect("usuarios.db")

cursor = conn.cursor()

# Crear tabla
cursor.execute('''
                CREATE TABLE IF NOT EXISTS Usuarios(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nombre TEXT
               )
                ''')

cursor.execute('''
                CREATE TABLE IF NOT EXISTS Tareas(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nombre TEXT,
               idUsuario INTEGER,
               completada BOOLEAN
               )
                ''')

# Crear clases
class Usuarios:
    def __init__(self, nombre):
        self.nombre = nombre

    def registraUsuario(self):
        try:
            cursor.execute("INSERT INTO Usuarios (nombre) VALUES (?)", (self.nombre,))
            conn.commit()  # Asegurarse de guardar los cambios
        except Exception as e:
            print(f"Error: {e}")

class Tareas:
    def __init__(self, nombre, idUsuario, completada):
        self.nombre = nombre
        self.usuario = idUsuario
        self.completada = completada

    def creaTarea(self):
        try:
            cursor.execute("INSERT INTO Tareas (nombre, idUsuario, completada) VALUES (?, ?, ?)",
                           (self.nombre, self.usuario, 1 if self.completada else 0))
            conn.commit()  # Asegurarse de guardar los cambios
        except Exception as e:
            print(f"Error: {e}")

    def consultaTareas(self):
        try:
            cursor.execute("SELECT * FROM Tareas")
            tareas = cursor.fetchall()
            for tarea in tareas:
                print(f"Tarea ID: {tarea[0]}, Nombre: {tarea[1]}, Usuario ID: {tarea[2]}, Completada: {tarea[3]}")
        except Exception as e:
            print(f"Error: {e}")

    def marcaCompleta(self, idTarea):
        try:
            cursor.execute("UPDATE Tareas SET completada = ? WHERE id = ?", ('si', idTarea))
            conn.commit()  # Asegurarse de guardar los cambios
        except Exception as e:
            print(f"Error: {e}")

def menu():
    while(True):
        print("OPCIONES")
        print("1. Registra usuario")
        print("2. Asigna tarea a usuario")
        print("3. Consulta tareas pendientes y completadas de cada usuario")
        print("4. Marcar tareas como completadas")
        print("5. Guardar y recuperar la información desde una BD SQLite")
        print("6. Salir")

        opcion = int(input("Elige una opción: ")) 

        match opcion:
            case 1:
                nombre = input("Dime el nombre del usuario: ")
                usuario = Usuarios(nombre)
                usuario.registraUsuario()

            case 2:
                nombre = input("Dime el nombre de la tarea: ")
                idUsuario = int(input("A qué usuario quieres asignar la tarea?: "))
                completada = input("Está completada la tarea? (si/no): ").strip().lower() == "si"
                tarea = Tareas(nombre, idUsuario, completada)
                tarea.creaTarea()

            case 3:
                tarea = Tareas('', 0, False)  # Crear instancia para llamar a consultaTareas
                tarea.consultaTareas()
            
            case 4:
                idTarea = int(input("Qué tarea quieres marcar como completada?: "))
                tarea = Tareas('', 0, False)  # Crear instancia para llamar a marcaCompleta
                tarea.marcaCompleta(idTarea)

            case 5:
                # Recuperar todos los usuarios
                cursor.execute("SELECT * FROM Usuarios")
                usuarios = cursor.fetchall()
                for usuario in usuarios:
                    print(f"Usuario ID: {usuario[0]}, Nombre: {usuario[1]}")
                
                # Recuperar todas las tareas
                cursor.execute("SELECT * FROM Tareas")
                tareas = cursor.fetchall()
                for tarea in tareas:
                    print(f"Tarea ID: {tarea[0]}, Nombre: {tarea[1]}, Usuario ID: {tarea[2]}, Completada: {tarea[3]}")
            
            case 6:
                print("Saliendo...")
                break  # Salir del loop

# Ejecutar el menú
menu()

# Cerrar la conexión al final
conn.close()
