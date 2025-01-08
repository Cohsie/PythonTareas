

def reemplazaVocales():
    frase = input("Introduce la frase que quieres reemplazar: ")
    nueva_frase = ''
    for char in frase:
        if char in 'aeiouAEIOU':
            nueva_frase += '*'
        else:
            nueva_frase += char
    print(nueva_frase)

def mensajeNumero():
    cantidad = int(input("Cuántos números se van a introducir?: "))
    numeros = []
    for _ in range(cantidad):
        num = int(input("Dime el número: "))
        if numeros:
            if num <= numeros[-1]:
                print("El número no es mayor")
        numeros.append(num)
    
def masLarga():
    frase = input("Dime una frase")
    palabras = frase.split()
    palabraLarga = " "
    for palabra in palabras:
        if len(palabra) > len(palabraLarga):
            palabra = palabraLarga
    print("La palabra más larga es: " + palabraLarga)

def rectanguloImpar():
    filas = int(input("Introduce el número de filas: "))
    columnas = int(input("Introduce el número de columnas: "))
    counter = 1
    for i in range (filas):
        for j in range (columnas):#Cuando termina de escribir los números de las columna se salta un párrafo y va a la siguiente fila. Y se repite.
            print(counter, end=" ")
            counter += 2
        print("\n")#Salto de párrafo
        if counter >= 100:
            break


def aparicionCaracter():
    palabra = input("Dime una palabra: ")
    resultado = contar_caracteres(palabra)
    for char, count in resultado.items():#.items es para las 2 partes de un diccionario
        print(f"{char}: {count}")


def contar_caracteres(palabra):
    conteo = {}
    for char in palabra:
        if char != ' ':
            if char in conteo:#Si el carácter está en conteo
                conteo[char] +=1#Súmale 1 a la posición en la que ya está
            else:
                conteo[char] = 1#Mételo en conteo y dale el valor de 1
    return conteo

def menu():
    while(True):

        print("OPCIONES")
        print("a. Reemplaza vocales por *")
        print("b. Di si el ultimo numero es mayor que el otro")
        print("c. Averigua la palabra más larga")
        print("d. Escribe un rectángulo de impares")
        print("e. Cuenta el número de veces que aparece un carácter")
        opcion = input("Introduce una opción: ")

        match opcion.lower():
            case 'a':
                reemplazaVocales()
            case 'b':
                mensajeNumero()
            case 'c':
                masLarga()
            case 'd':
                rectanguloImpar()
            case 'e':
                aparicionCaracter()

menu()
            