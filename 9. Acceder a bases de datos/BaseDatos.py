import sqlite3
conn = sqlite3.connect('base_datos_prueba.db')

cursor = conn.cursor()

#Creación de tabla
cursor.execute('''
               CREATE TABLE IF NOT EXISTS usuarios(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nombre TEXT,
               edad INTEGER
               )
               ''')

#Insertar datos
cursor.execute('INSERT INTO usuarios (nombre, edad) VALUES (?, ?)', ('Juan Pedro', 34))

#Confirmar cambios
conn.commit()

#Consultar datos
cursor.execute('SELECT * FROM usuarios')
print(cursor.fetchall())

#Cerrar conexion
conn.close()