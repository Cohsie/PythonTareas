# 2.Escribe un programa que lea una cadena y devuelva un diccionario con
# la cantidad de apariciones de cada carácter en la cadena.

texto = input("Dime una frase: ")

conteo = {}

for char in texto: #Se crea una variable que recorre texto y se encarga de contar la aparición de cada caracter
    if char in conteo:
        conteo[char] += 1 #Si esa variable está en el texto le suma 1 a su valor (char es key y el número es value)
    else:
        conteo[char] = 1 #Si esta variable no está en el texto se añade y se le da un valor inicial de 1
print(conteo)