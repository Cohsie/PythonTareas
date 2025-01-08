# 7. # Definir la función
# finales : (int, list[A]) -> list[A]
# tal que finales(n, xs) es la lista formada por los n finales
# elementos de xs. Por ejemplo,
# finales(3, [2, 5, 4, 7, 9, 6]) == [7, 9, 6]

from typing import List, TypeVar

A = TypeVar('A')

Lista = []

n = input("Introduce un número. Espacio para terminar")

while n != " ":
    Lista.append(int(n))
    n =input("Otro número: ")

def finales(n:int, lst:list[A]) -> list[A]:
    return lst[-n:]

finElemento = int(input("Escribe la cantidad de elementos totales que quieres coger de la lista: "))
print(f"Lista original: {Lista}")
print(f"Elementos finales deseados: {finales(finElemento, Lista)}")