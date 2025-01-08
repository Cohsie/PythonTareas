# Biblioteca donde mirar en el examen

# !MENU, WHILE Y TRY-EXCEPT --------------------------------------------------------
def main():

    opcion=""

    while opcion!="h":
        
        
        print("Bienvenido al menú:\n")
        print("a)Mostrar un rombo.")
        print("b)Adivinar un número.")
        print("c)Resolver un ecucación de segundo grado.")
        print("d)Tabla de números.")
        print("e)Cálculo del número factorial de un número.")
        print("f)Cálculo de un número de la sucesión de Fibonacci.")
        print("g)Tabla de multiplicar.")
        print("h)Salir.\n")

        opcion=str(input("Dime una opcion:\n")).lower()   #Para que de igual si pones mayusculas o minusculas

        #Ahora controlamos la letra que meta
        match opcion:
            case "a":
                print("Hola")
            case "b":
                print("Hola")
            case "c":
                print("Hola")
            case "d":
                print("Hola")
            case "e":

                #! Bucle while para hacer hasta que pongamos break 
                while True:
        
                    #! Try para el tema del número 
                    try:

                        n=int(input("Dime un numero para hacer su factorial:"))
                        
                        if (n<0):
                            print("No se puede hacer factorial con numeros negativos.\n")
                            continue  #Puedo poner continue o el resto de código ponerlo en un else
                        
                        r=factorial(n)
                        print("El factorial de",n,"es:",r)
                        break    #!Aqui cuando llega el bucle separa, el bucle es que para cuanod entra un valor correcto

                    except ValueError:
                        print("Por favor, introduce valores numéricos.\n")

            case "f":
                print("Hola")
            case "g":
                print("Hola")
            case "h":
                print("Saliendo del programa, que tenga un buen dia.\n")
            case _:
                print("Opción no válida. Por favor, selecciona una opción válida.\n")

if __name__=="__main__":
    main()


# ! LISTAS--------------------------------------------------------------------------

lista = []
lista.append()
lista.reverse()
lista.sort()
lista = cadena.split()          #SPLIT divide la cadena en solo palabras
# Bucle para recorrerlo
for i in lista:
    print(i, end=" ")
# Bucle de un punto a otro
for i in range(n, len(lista)):
        resultado.append(lista[i])

# !FUNCIONES------------------------------------------------------------------------
# s:str, le digo a s que es un string / -> bool le estoy diciendo que devuelve un booleano
def palindromo(s:str) -> bool:

    s = s.replace(" ", "").lower()

    # Su versión invertida
    return s == s[::-1]

# El if in es muy importante
for i in cadena.lower():
        if i in vocales:
            contador += 1

# !TUPLAS----------------------------------------------------------------------------


# !DICCIONARIOS----------------------------------------------------------------------
# !Ejercicio4 y EjercicioMenu son buenos para mirar estas cosas
# Creación de diccionarios
vacio = {}
precios = {"Pera":1.60, "Ciruela": 1.24,"Manzana": 1.75}

vacio = dict()
precios = dict(Pera=1.60, Ciruela=1.24,Manzana=1.75)

# Añadir o modificar un elemento:
precios["Sandía"] = 0.99

# Comprobar si una clave existe en el diccionario sin errores para obtener su valor:
pSandia = precios.get("Sandía")

if "Pera" in precios:
    pSandia = precios["Pera"]

# Borrar un elemento
del precios["Sandia"]

# Obtener un elemento y eliminarlo, para que no ocurra error se pone el -1, ya que es el valor por defecto que devolvera si Sandia no existe
precio_sandia = precios.pop("Sandia", -1)

# Vaciar el diccionario
precios.clear()

# Longitud del diccionario
len(precios)

# Funciones
if "Pera" in precios.keys()  if "Pera" in precios #Es lo mismo

precios.values()        #Devuelve solo los valores
precios.items()         #Devuelve una lista con todo

# SI pongo items en el for puedo coger las dos cosas a la vez
print("\nListado de alumnos y sus notas medias:")
for nombre, notas in alumnos.items():

    # si hay notas 
    if notas :  
        media = sum(notas) / len(notas)
        print(nombre,": Nota media = ",media)
    else:
        print(nombre, " no tiene notas registradas.")

# !Si hago un for y quiero hacerlo un numero concreo puedo hacer:
num_alumnos = int(input("Dime el numero de alumnos: "))

# for i in range(num_alumnos):




# !USANDO CLASES Y DICCIONARIOS
class Persona:
    def __init__(self, nombre, edad, email):
        self.__nombre = nombre
        self.__edad = edad
        self.__email = email
    
    # Getter de nombre
    @property
    def nombre(self):
        return self.__nombre
    
    
    # Setter de nombre
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre
    
    
    # Getter de edad
    @property
    def edad(self):
        return self.__edad
    
    
    # Setter de edad
    @edad.setter
    def edad(self, edad):
        self.__edad = edad
    
    
    # Getter de email
    @property
    def email(self):
        return self.__email
    
    
    # Setter de email
    @email.setter
    def email(self, email):
        self.__email = email

    def __str__(self): 
        return f"Persona: Nombre= {self.__nombre}, Edad= {self.__edad}, Email= {self.__email}"



# Metodos -----------------------------------------------------------------------------------------
def agregar_persona(diccionario):

    # Pedimos lo cenesariopara el objeto
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    email = input("Email: ")

    # Creamos el objeto
    persona = Persona(nombre, edad, email)

    # Dentro del diccionario ponemos como clave su nombre y como valor el objeto
    diccionario[nombre] = persona
    print(f"Persona {nombre} agregada correctamente.")


def eliminar_persona(diccionario):

    nombre = input("Nombre de la persona a eliminar: ")

    # Si el nombre que nos pasa está en el diccionario lo borramos
    if nombre in diccionario:
        del diccionario[nombre]
        print(f"Persona {nombre} eliminada correctamente.")
    else:
        print(f"No se encontró la persona con el nombre {nombre}.")


def mostrar_personas(diccionario):

    # Asi confirmo si hay valores en el diccionario
    if diccionario:
        print("\n--- Lista de Personas ---")
        for persona in diccionario.values():
            print(persona.__str__())
    else:
        print("No hay personas registradas.")


def buscar_persona(diccionario):
    nombre = input("Nombre de la persona a buscar: ")
    if nombre in diccionario:
        print(diccionario[nombre])
    else:
        print(f"No se encontró la persona con el nombre {nombre}.")

# Main ---------------------------------------------------------------------------------------------
def main():

    # Creacion del diccionario
    personas = {}

    while True:
        opcion = input("Elige una opción (1-5): ")
        
        if opcion == "1":
            agregar_persona(personas)
        elif opcion == "2":
            eliminar_persona(personas)
        elif opcion == "3":
            mostrar_personas(personas)
        elif opcion == "4":
            buscar_persona(personas)
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    main()