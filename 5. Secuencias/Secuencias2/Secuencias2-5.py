# 5. Definir la función
# rango : (List[int]) -> List[int]
# tal que rango(xs) es la lista formada por el menor y mayor elemento
# de xs.
# rango([3, 2, 7, 5]) == [2, 7]

from typing import List

Lista = []
n = input("Introduce numero para la lista. Espacio termina")

while n != " ":
    Lista.append(int(n))
    n = input("Dame otro número")

inicio = int(input("Dime el inicio del rango"))
final = int(input("Dime el final del rango"))

def rango (lst: List[int]) -> List[int]:
    return lst[inicio:final]



print(f"Lista sobre la que se actúa {Lista}")
print(f"Rango seleccionado: {inicio} {final}. Resultado: {rango(Lista)}")
