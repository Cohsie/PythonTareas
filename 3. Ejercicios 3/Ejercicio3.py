#Escribe un programa que recoja números por teclado hasta que se introduzca
#el valor cero. A continuación, debe mostrar el número de valores introducidos,
#el valor mínimo introducido, el máximo, la suma de todos ellos y su media
#aritmética (todos los cálculos sin contar el cero)

counter = 0

lista=[]
valor = int(input("introduce un valor"))
while valor !=0:
    lista.append(valor)
    valor = int(input("introduce un valor"))

print("El nº de valores es: ", len(lista))
print("El máximo es: ", max(lista))
print("El máximo es: ", min(lista))
print("La media es: ", sum(lista)//len(lista))

