

def reemplazarVocal():
    palabra =  input("Dime una palabra")
    nuevaPalabra = ''#Creas un string

    for char in palabra:#Recorres la palabra original
        if char == 'aeiouAEIOU':#Y por cada vocal llenas el nuevo string con *
            nuevaPalabra += '*'
        else:
            nuevaPalabra += palabra#Si no es vocal lo llenas con caracteres normales
    print(nuevaPalabra)#E imprimes el string nuevo con los cambios hechos


def numMayor():
    cantidad = int(input("Escribe la cantidad de números: "))
    numeros = []

    for _ in range (cantidad):
        num = int(input("Escribe un número: "))
        if numeros:
            if num <= numeros[-1]:
                print("No es mayor")
        numeros.append(num)

def palabraLarga():
    frase = input("Escribe una frase: ")
    palabras = frase.split()
    palabraLarga= ''
    for palabra in palabras:
        if len(palabra) < len(palabraLarga):
            palabra = palabraLarga
    print("La palabra más larga es " + palabraLarga)

def rectangulo():
    fila = int(input("Dime el número de filas: "))
    columna =  int(input("Dime el número de columnas: "))
    counter = 1
    for i in range (fila):
        for j in range (columna):
            print(counter, end=' ')
            counter +=2
        print("/n")#Salto de columna para la fila
        if counter >= 100:
            break








def menu ():
    while (True):
        print("OPCIONES")
        print("a. Reemplazar vocales de una frase")
        print("b. Numero no mayor que el primero")
        print("c. Palabra más larga")
        print("d. Rectángulo con impares hasta 100")
        print("e. Aparicion de cada carácter")