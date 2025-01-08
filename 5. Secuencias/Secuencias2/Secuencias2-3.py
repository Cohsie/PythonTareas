a = int(input("Escribe el primer número: "))
b = int(input("Escribe el segundo número: "))
c = int(input("Escribe el tercer número: "))


def sumaNumeros(a, b):
    d = a+b
    return d

sumaTotal = c + sumaNumeros(a, b)
print("La suma total de los 3 números es: ", sumaTotal)