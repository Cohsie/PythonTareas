numeros = []


while True:

    num = int(input("Introduce un número, 0 para terminar: "))

    if num == 0:
        break

    numeros.append(num)

    print(numeros)

    numeros.sort()
    print(numeros)

    numeros.sort(reverse = True)
    print(numeros)



