texto = input("Escribe un texto para ver si es palíndromo: ")

if len(texto) >= 3 and texto == texto[::-1]:
    print("El texto es palíndromo")
else:
    print("No es palíndromo")