'''NOMBRE Y APELLIDOS: Jose Antonio Torres Barrachina
Desarrolla un programa en Python que gestione un sistema de biblioteca.No hace falta que comentes cada cosa que realices pero sí lo que consideres debería saber otro compañero tuyo, para cuando te vayas de vacaciones y tu compañero debe manipular tu código. Este programa debe cumplir los siguientes requisitos:

1.Define una clase base Material que tenga atributos comunes a todos los materiales de la biblioteca, como:
id (único para cada material)
título
autor
año de publicación 
2.Crea dos clases que hereden de Material:

Libro: Incluye atributos adicionales como género (debe seleccionarse entre una lista predefinida: "Ficción", "No Ficción", "Terror", "Ciencia") y número de páginas (debe ser mayor a 0).

Revista: Incluye atributos adicionales como número de edición y mes de publicación (debe seleccionarse entre los meses válidos: "Enero", "Febrero", ..., "Diciembre")

3.Utiliza un diccionario para almacenar los materiales, donde la clave sea el id y el valor sea un objeto de tipo Libro o Revista.

4.Mantén una lista de todos los id existentes para verificar que no se repitan al agregar nuevos materiales.

5. Generar Estadísticas:debe devolver todos estos valores
Total de materiales registrados.
Número de libros y revistas.
Promedio de páginas para los libros.
Ayuda: se puede usar la siguiente función: Ej: isinstance(m, Libro)--> devuelve true si el objeto m es de tipo Libro

6.Implementa un menú que permita al usuario realizar las siguientes acciones:
Agregar Material: Permite al usuario agregar un nuevo Libro o Revista.
Listar Materiales: Muestra una lista de todos los materiales registrados con sus detalles. Elije la forma de presentación más adecuada para que el usuario lo vea claro.
Buscar Material por ID: Permite al usuario buscar un material específico por su id.
Eliminar Material: Elimina un material específico usando su id.
Generar Estadísticas
Salir: Termina la ejecución del programa.'''


class Material:
    def __init__(self, id, titulo, autor, anio_publicacion):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion

class Libro (Material):#Clase que hereda de Material
    def __init__(self, id, titulo, autor, anio_publicacion, genero, numero_paginas):
        super().__init__(id, titulo, autor, anio_publicacion)
        self.genero = genero
        self.numero_paginas = numero_paginas

    def __str__(self):
        return f"ID: {self.id}: titulo: {self.titulo}, Año: {self.anio_publicacion}, genero: {self.genero}, numero de paginas: {self.numero_paginas}"

class Revista (Material):#Clase que hereda de Material
        def __init__(self, id, titulo, autor, anio_publicacion, numero_edicion, mes_publicacion):
            super().__init__(id, titulo, autor, anio_publicacion)
            self.numero_edicion = numero_edicion
            self.mes_publicacion = mes_publicacion

        def __str__(self):
            return f"ID: {self.id}: titulo: {self.titulo}, Año: {self.anio_publicacion}, numero de edicion: {self.numero_edicion}, mes de publicacion: {self.mes_publicacion}"

Diccionario = {}
ListaId = []#Lista creada para asegurar que no haya varios materiales con el mismo id
generos =["ficcion", "no ficcion", "terror", "ciencia"]#Estos son los géneros válidos que puede introducir el usuario
meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "ocotubre", "noviembre", "diciembre"]#Los meses del año para introducir una revisto
def agregarMaterial():
    #Permite añadir un material al diccionario
    aniadir = int(input("Quieres añadir un libro (escribe 1) o una revista (escribe 2)"))
    if aniadir == 1:
        id = (input("Introduce el id del material: "))
        titulo = input("Introduce el titulo: ")
        autor = input("Introduce el nombre del autor: ")
        anio_publicacion = int(input("Introduce el año de publicación: "))

        while True:
            try:
                genero = input("Dime el género: ")

                if genero not in generos:
                    raise ValueError("Género no válido")#Si el genero no está en la lista generos da error
                break
            except ValueError as e:
                print(f"Error: {e}. Intenta de nuevo.")

        while True:
            try:
               num_paginas = int(input("Dime el número de páginas: ")) 
               if num_paginas < 0:
                   raise ValueError("El número de páginas no es válido")#Si el número de páginas es negativo da error
               break
            except ValueError as e:
                print(f"Error: {e}. Intenta de nuevo.")
        
        if id not in ListaId:
            Literatura = Libro(id, titulo, autor, anio_publicacion, genero, num_paginas)
            Diccionario[id] = Literatura
            print(f"Material {id} añadido.")
            ListaId.append(id)
        else:
            print("Ya existe un material con ese id.")

    elif aniadir == 2:
        id = (input("Introduce el id del material: "))
        titulo = input("Introduce el titulo: ")
        autor = input("Introduce el nombre del autor: ")
        anio_publicacion = int(input("Introduce el año de publicación: "))
        numero_edicion = int(input("Dime el número de edición: "))

        while True:
            try:
                mes_publicacion= input("Dime el mes de publicación: ") 
                if mes_publicacion not in meses:
                    raise ValueError("Debes introducir uno de los meses del año")
                break
            except ValueError as e:
                print(f"Error: {e}. Intenta de nuevo.")

        if id not in ListaId:
            Literatura = Revista(id, titulo, autor, anio_publicacion, numero_edicion, mes_publicacion)
            Diccionario[id] = Literatura
            print(f"Material {id} añadido.")
            ListaId.append(id)
        else:
            print("Ya existe un material con ese id.")
    else:
        print("No válido. Debes escribir entre 1 y 2")

def listarMateriales():
    for clave, valor in sorted(Diccionario.items()):#Recorre todo el Diccionario para listar todas las instancias de los materiales
        print (clave, valor)

def buscarMaterial():
    id = int(input("Introduce el id del material que quieres buscar: "))
    for id in Diccionario.keys():
        print(Diccionario[id])
        break
    else:
        print("Ese material no existe.")

def eliminarMaterial():
    id = int(input("Introduce el id del material que quieres aliminar: "))
    for id in Diccionario.keys():#Recorre el Diccionario para encontrar el id solicitado
        del Diccionario[id]
        print(f"Material con {id} eliminado correctamente.")
        break
    else:
        print("Ese material no existe en la biblioteca.")

#def generarEstadisticas():

def menu():
    while(True):

        print("OPCIONES")
        print("1. Agregar nuevo material")
        print("2. Listar materiales")
        print("3. Buscar material")
        print("4. Eliminar material")
        print("5. Generar estadísticas")
        opcion = int(input("Introduce una opción: "))

        match opcion:
            case 1:
                agregarMaterial()
            case 2:
                listarMateriales()
            case 3:
                buscarMaterial()
            case 4:
                eliminarMaterial()
            case 5:
                generarEstadisticas()
            case 6:
                print("Saliendo...")
                break
            case default:
                print("Opcion no válida")