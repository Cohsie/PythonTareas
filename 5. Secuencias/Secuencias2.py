textos = []

while True:
    txt = input("Escribe una palabra, espacio para terminar: ")

    if txt == " ":
        break

    textos.append(txt)
    print(textos)

    textos.sort()
    print(textos)

    textos.sort(reverse=True)
    print(textos)