import math
import random

def mostrarRombo():

    num = int(input("Dame un número"))
    asterisco = "*"
    counter = 0
    if num % 2 == 0:
        print("Número no válido")
    else:    
        while counter < num:
            print(asterisco)
            asterisco += "*"
            counter += 1
        while counter == num and len(asterisco) > 0:
            asterisco = asterisco [:-1]
            print(asterisco)

def adivinarNumero():
    random.randint(1-100)
    num = int(input("Adivina el número illo"))

    while True:
        if num == random:
            print("¡Correcto!")
            break
        elif num < random:
            print("El número es mayor")
        elif num > random:
            print("El número es menor")

def resolverEcuacion():
    a = int(input("dime el primer numero"))
    b = int(input("Dime el segundo numero"))
    c = int(input("Dime el tercer número"))

    form = b*b-4*a*c

    if form < 0:
        print("La ecuación no tiene solución")
    else:
        x1 = (-b + math.sqrt(b**2-4*a*c)) / (2*a)
        x2 = (-b - math.sqrt(b**2-4*a*c)) / (2*a)
        print(x1)
        print(x2)

def tablaNumero():

    fil = int(input("Dime numero de filas"))
    col = int(input("Dime numero de columnas"))

    random.randint(1-100)

    for i in range(fil):
        for j in range(col):
            print(random, "\t", end="")
            counter +=1
        print("\n")

def factorial():

    num = int(input("Di un numero"))

    i = num

    while i > 1:
        num = num * (i-1)
        i-=1
    
    print(num)

def fibonacci():
    num = int(input("Di una posición de fibonacci"))

    ini = 0
    counter = 0
    a = 1
    b = 0
    while counter < num:
        a + b
        b = a + b
        print (a + b)
    
def multiplicar():
    num = int(input("Dime el número para ponerte la tabla: "))

    print(num, "x 1 = ", num)
    print(num, "x 2 = ", num*2)
    print(num, "x 3= ", num*3)
    print(num, "x 4 = ", num*4)
    print(num, "x 5 = ", num*5)
    print(num, "x 6 = ", num*6)
    print(num, "x 7 = ", num*7)
    print(num, "x 8 = ", num*8)
    print(num, "x 9 = ", num*9)
    print(num, "x 10 = ", num*10)


def menu():
    match opcion:
        case "a":
            print("Has elegido mostrar un rombo")
            mostrarRombo()
        case "b":
            print("Has elegido adivinar un número")
            adivinarNumero()
        case "c":
            print("Has elegido resolver una ecuación de segundo grado")
            resolverEcuacion()
        case "d":
            print("Has elegido tabla de numeros")
            tablaNumero()
        case "e":
            print("Has elegido calculo factorial")
            factorial()
        case "f":
            print("Has elegido calculo de fibonacci")
            fibonacci()
        case "g":
            print("Has elegido tabla de multiplicar")
            multiplicar()
        case "h":
            print("Saliendo del programa...")
        case default:
            print("Opción no válida")

print("a. Mostrar un rombo")
print("b. Adivinar un número")
print("c. Resolver una ecuación de segundo grado")
print("d. Tabla de numeros")
print("e. Calculo del numero factorial de un numero")
print("f. Calculo de un numero de la sucesion de fibonacci")
print("g. Tabla de multiplicar")
print("h. Salir")
opcion = input("Dime una opcion: ")    
