#6. Definir la función
# interior : (list[A]) -> list[A]
# tal que interior(xs) es la lista obtenida eliminando los extremos de
# la lista xs. Por ejemplo,
# interior([2, 5, 3, 7, 3]) == [5, 3, 7]

from typing import List, TypeVar

A = TypeVar('A')

Lista = []
n = input("Introduce un número para la lista. Espacio termina: ")

while n != " ":
    Lista.append(int (n))
    n = input("Otro número")

def interior (lst: list[A]) -> list[A]:
    if len(lst) > 1:
        return lst[1:-1]
    else:
        return []

print(f"Lista original: {Lista}")
print(f"Lista con bordes quitados: {interior(Lista)}")