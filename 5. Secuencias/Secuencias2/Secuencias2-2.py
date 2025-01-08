def cadenaTexto(palabra):
    counter = 1
    if palabra:
        for letra in palabra:
            if letra in " ":
                counter += 1
    else:
        print("No has escrito nada")
        counter = 0
    print(counter)


palabra = input("Escribe una frase: ")
cadenaTexto(palabra)