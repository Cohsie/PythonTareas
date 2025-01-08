#Escribe un programa que recoja un número de filas y columnas, y muestre una
#tabla con tantas filas y columnas como indicadas, numerando las celdas de
#izquierda a derecha y de arriba abajo. Por ejemplo, si se introducen 2 filas y 3
#columnas, se debe mostrar:
#1 2 3
#4 5 6

fil = int(input("Escribe el número de filas"))
col = int(input("Escribe el número de columnas"))

counter = 1

for i in range(fil):
    for j in range(col):
        print(counter ,"\t", end="")
        counter +=1
    print("\n")