#3. Vamos a crear un programa en python donde vamos a declarar un
#diccionario para guardar los precios de las distintas frutas. El
#programa pedirá el nombre de la fruta y la cantidad que se ha vendido
#y nos mostrará el precio final de la fruta a partir de los datos
#guardados en el diccionario. Si la fruta no existe nos dará un error.
#Tras cada consulta el programa nos preguntará si queremos hacer otra
#consulta.

frutas = {
    "pera": 1.50,
    "melocoton": 2,
    "naranja": 1.60,
    "platano": 1.75
}


pedir = input("Dime el nombre de la fruta: ").lower()
cantidad = int(input("Dime el número de esa fruta que se ha vendido: "))

if pedir in frutas:# Es igual a si hiciera if pedir in frutas.keys():
    print((frutas[pedir]) * cantidad)
else:
    print("Esa fruta no está")